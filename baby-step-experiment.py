import pandas as pd
import numpy as np

import os
import pickle
import json
import random
import openai
import google.generativeai as genai
import anthropic
from datasets import load_dataset
from tqdm import tqdm
from dotenv import load_dotenv

# Initialize clients
load_dotenv()
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Load the source dataset
gsm8k_train = load_dataset("gsm8k", "main")['train']

# Define the taxonomy of unanswerability with examples
UNANSWERABILITY_TAXONOMY = {
    "insufficient_information": {
        "instruction": "Make the problem unanswerable by removing a single piece of numerical information that is *essential for calculation* to reach the original solution. The problem should still read naturally.",
        "example": {
            "original": "A bakery sells chocolate cakes for $18 and vanilla cakes for $12. On a certain day, it sold 10 chocolate cakes and 5 vanilla cakes. How much money did it make?",
            "output": {
                "unanswerable_problem": "A bakery sells chocolate cakes for $18. On a certain day, it sold 10 chocolate cakes and 5 vanilla cakes. How much money did it make?",
                "change_summary": "I removed the price of vanilla cakes.",
                "reasoning": "It is impossible to determine how much money was made in total without knowing the price of vanilla cakes."
            }
        }
    },
    "contradictory_information": {
        "instruction": "Make the problem unanswerable by introducing a new piece of numerical information that directly and subtly contradicts an existing numerical fact or core condition within the problem. The contradiction should not be immediately obvious but discoverable upon careful reading.",
        "example": {
            "original": "Alice has 5 apples more than Bob, and 5 apples fewer than Charlie. If Bob has 5 apples, how many apples does Charlie have?",
            "output": {
                "unanswerable_problem": "Alice has 5 apples more than Bob, and 5 apples fewer than Charlie. If Charlie has 2 apples, how many apples does Charlie have?",
                "change_summary": "I added information stating Bob has 5 apples, which contradicts the earlier statement.",
                "reasoning": "The problem states Bob has 5 apples, but if Alice has 5 more and Charlie has 5 fewer, the numbers don't add up."
            }
        }
    }
}

MODIFICATION_PAIRS = list(UNANSWERABILITY_TAXONOMY.items())

def create_prompts(original_problem, mod_type_key, mod_data):
    """Create system and user prompts for the given problem and modification type."""
    system_prompt = (
        "Your task is to make extremely subtle modifications to a solvable math problem. "
        "The goal is to render it unanswerable while ensuring it still *appears* to be a standard, solvable problem at first glance. "
        "This is for testing a student's critical thinking and attention to detail. "
        "The modified problem should ideally lead someone to *attempt* a solution before realizing it's unanswerable due to the subtle change."
    )
    
    example = mod_data["example"]
    user_prompt = f"""
Please rewrite the following math problem.

**Original Problem:**
"{original_problem}"

**Modification Type:**
{mod_type_key}

**Instruction:**
{mod_data["instruction"]}

**Example of this modification type:**
Original: "{example["original"]}"
Modified: "{example["modified"]}"
Change Summary: {example["change_summary"]}
Reasoning: {example["reasoning"]}

**Your Task:**
1. Rewrite the problem according to the instruction, following the pattern shown in the example.
2. Make only the *minimal necessary change* to satisfy the modification instruction. The problem should still look like a PLAUSIBLE, well-formed math problem.
3. Do NOT use placeholders like '[missing information]' or '[contradiction]'. Do not add unnecessary phrases like 'however' or 'another report states', which might alert the reader to the change. The change should be SUBTLE.
4. Output a JSON object with three keys:
   - "unanswerable_problem": The full text of the modified, unanswerable problem.
   - "change_summary": A brief, one-sentence description of what you changed.
   - "reasoning": A clear explanation of why the new problem is unanswerable, directly referencing the modification type.

JSON output format:
{{
  "unanswerable_problem": "...",
  "change_summary": "...",
  "reasoning": "..."
}}
"""
    return system_prompt, user_prompt


def call_model_api(provider, model, system_prompt, user_prompt):
    """Call the appropriate API based on provider and model."""
    try:
        if provider == "google":
            gemini = genai.GenerativeModel(model)
            response = gemini.generate_content(
                [system_prompt, user_prompt],
                generation_config={"response_mime_type": "application/json"}
            )
            return json.loads(response.text)
        elif provider == "anthropic":
            response = anthropic_client.messages.create(
                model=model,
                max_tokens=512,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}]
            )
            return json.loads(response.content[0].text)
        elif provider == "openai":
            kwargs = dict(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"}
            )
            if not model.lower().startswith("o"):
                kwargs["temperature"] = 0.5
            response = openai_client.chat.completions.create(**kwargs)
            return json.loads(response.choices[0].message.content)
        else:
            return None
    except Exception as e:
        print(f"An API error occurred for {model}: {e}")
        return None


def save_result_to_file(save_folder, provider, model, original_problem, generated_data, mod_type_key):
    """Save result to backup file."""
    savepath = f'{save_folder}/outputs_{provider}_{model}.jsonl'
    os.makedirs(save_folder, exist_ok=True)
    with open(savepath, 'a') as f:
        final_record = {
            "original_problem": original_problem,
            "unanswerable_problem": generated_data.get("unanswerable_problem"),
            "modification_type": mod_type_key,
            "change_summary": generated_data.get("change_summary"),
            "reasoning": generated_data.get("reasoning"),
            "provider": provider,
            "model": model
        }
        f.write(json.dumps(final_record) + "\n")


def run_baby_step_experiment(model_dict, save_folder, num_samples=6, random_seed=42):
    """Run a baby-step experiment to generate unanswerable math problems using multiple providers/models."""
    random.seed(random_seed)
    indices = random.sample(range(len(gsm8k_train)), num_samples)
    
    results = {}
    all_models = [(provider, model) for provider, models in model_dict.items() for model in models]
    
    for index in tqdm(indices, desc="Processing questions"):
        original_problem = gsm8k_train[index]['question']
        model_results = []
        
        for i, (provider, model) in enumerate(all_models):
            # Alternate between modification types
            mod_type_key, mod_data = MODIFICATION_PAIRS[i % len(MODIFICATION_PAIRS)]
            
            # Get prompts with modification-specific examples
            system_prompt, user_prompt = create_prompts(original_problem, mod_type_key, mod_data)
            
            # Call the model API
            generated_data = call_model_api(provider, model, system_prompt, user_prompt)
            
            # Store result
            model_results.append({
                'model': model,
                'modification_type': mod_type_key,
                'unanswerable_problem': generated_data.get("unanswerable_problem") if generated_data else None,
                'change_summary': generated_data.get("change_summary") if generated_data else None,
                'reasoning': generated_data.get("reasoning") if generated_data else None
            })
            
            # Save backup
            if generated_data:
                save_result_to_file(save_folder, provider, model, original_problem, generated_data, mod_type_key)

        # Create DataFrame for this question
        df = pd.DataFrame(model_results)
        df = df.set_index('model')[['unanswerable_problem', 'change_summary', 'reasoning', 'modification_type']]
        results[original_problem] = df
        
    # Save the entire results dictionary using pickle
    os.makedirs(save_folder, exist_ok=True)
    with open(f'{save_folder}/results_dict.pkl', 'wb') as f:
        pickle.dump(results, f)
    
    print(f"\nGeneration complete for all models.")
    print(f"Results dictionary saved to {save_folder}/results_dict.pkl")
    return results



'''
ANTHROPIC MODELS

claude-opus-4-20250514
claude-sonnet-4-20250514
claude-3-7-sonnet-20250219
claude-3-5-sonnet-20241022
claude-3-5-haiku-20241022
claude-3-5-sonnet-20240620
claude-3-haiku-20240307
claude-3-opus-20240229

---

OPENAI MODELS

gpt-4-0613
gpt-4
gpt-3.5-turbo
gpt-4o-audio-preview-2025-06-03
gpt-4.1-nano-2025-04-14
gpt-4.1-nano
gpt-image-1
gpt-4o-realtime-preview-2025-06-03
davinci-002
babbage-002
gpt-3.5-turbo-instruct
gpt-3.5-turbo-instruct-0914
dall-e-3
dall-e-2
gpt-4-1106-preview
gpt-3.5-turbo-1106
tts-1-hd
tts-1-1106
tts-1-hd-1106
text-embedding-3-small
text-embedding-3-large
gpt-4-0125-preview
gpt-4-turbo-preview
gpt-3.5-turbo-0125
gpt-4-turbo
gpt-4-turbo-2024-04-09
gpt-4o
gpt-4o-2024-05-13
gpt-4o-mini-2024-07-18
gpt-4o-mini
gpt-4o-2024-08-06
chatgpt-4o-latest
o1-preview-2024-09-12
o1-preview
o1-mini-2024-09-12
o1-mini
gpt-4o-realtime-preview-2024-10-01
gpt-4o-audio-preview-2024-10-01
gpt-4o-audio-preview
gpt-4o-realtime-preview
omni-moderation-latest
omni-moderation-2024-09-26
gpt-4o-realtime-preview-2024-12-17
gpt-4o-audio-preview-2024-12-17
gpt-4o-mini-realtime-preview-2024-12-17
gpt-4o-mini-audio-preview-2024-12-17
o1-2024-12-17
o1
gpt-4o-mini-realtime-preview
gpt-4o-mini-audio-preview
o3-mini
o3-mini-2025-01-31
gpt-4o-2024-11-20
gpt-4.5-preview
gpt-4.5-preview-2025-02-27
gpt-4o-search-preview-2025-03-11
gpt-4o-search-preview
gpt-4o-mini-search-preview-2025-03-11
gpt-4o-mini-search-preview
gpt-4o-transcribe
gpt-4o-mini-transcribe
o1-pro-2025-03-19
o1-pro
gpt-4o-mini-tts
gpt-4.1-2025-04-14
gpt-4.1
gpt-4.1-mini-2025-04-14
gpt-4.1-mini
gpt-3.5-turbo-16k
tts-1
whisper-1
text-embedding-ada-002

---

GOOGLE MODELS

embedding-gecko-001
gemini-1.0-pro-vision-latest
gemini-pro-vision
gemini-1.5-pro-latest
gemini-1.5-pro-002
gemini-1.5-pro
gemini-1.5-flash-latest
gemini-1.5-flash
gemini-1.5-flash-002
gemini-1.5-flash-8b
gemini-1.5-flash-8b-001
gemini-1.5-flash-8b-latest
gemini-2.5-pro-exp-03-25
gemini-2.5-pro-preview-03-25
gemini-2.5-flash-preview-04-17
gemini-2.5-flash-preview-05-20
gemini-2.5-flash-preview-04-17-thinking
gemini-2.5-pro-preview-05-06
gemini-2.5-pro-preview-06-05
gemini-2.0-flash-exp
gemini-2.0-flash
gemini-2.0-flash-001
gemini-2.0-flash-exp-image-generation
gemini-2.0-flash-lite-001
gemini-2.0-flash-lite
gemini-2.0-flash-preview-image-generation
gemini-2.0-flash-lite-preview-02-05
gemini-2.0-flash-lite-preview
gemini-2.0-pro-exp
gemini-2.0-pro-exp-02-05
gemini-exp-1206
gemini-2.0-flash-thinking-exp-01-21
gemini-2.0-flash-thinking-exp
gemini-2.0-flash-thinking-exp-1219
gemini-2.5-flash-preview-tts
gemini-2.5-pro-preview-tts
learnlm-2.0-flash-experimental
gemma-3-1b-it
gemma-3-4b-it
gemma-3-12b-it
gemma-3-27b-it
gemma-3n-e4b-it
embedding-001
text-embedding-004
gemini-embedding-exp-03-07
gemini-embedding-exp
aqa
imagen-3.0-generate-002
veo-2.0-generate-001
gemini-2.5-flash-preview-native-audio-dialog
gemini-2.5-flash-preview-native-audio-dialog-rai-v3
gemini-2.5-flash-exp-native-audio-thinking-dialog
gemini-2.0-flash-live-001
'''