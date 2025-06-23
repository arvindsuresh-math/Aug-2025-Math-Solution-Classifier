import pandas as pd
import numpy as np
import time

import importlib
import inspect
import os
import re
import json
import random
import openai
import google.generativeai as genai
import anthropic
from openai import OpenAI
from datasets import load_dataset
from tqdm import tqdm
from dotenv import load_dotenv

from typing import List, Dict, Any


# Initialize clients
load_dotenv()
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Load the GSM8K dataset (train split)
gsm8k_train = load_dataset("gsm8k", "main", split="train")


SYSTEM_PROMPT = "You are an expert Python programmer specializing in data formalization. Your role is to meticulously convert natural language math problems and their step-by-step solutions into a single, well-structured Python function. You will be presented with examples of the required format followed by a final task to complete."


PROMPT_GUIDELINES = """### Guidelines

0. **Output wrapping**
   Return the code inside a single ```python … ``` block, and nothing else.

1.  **Function Naming & Docstring:** The function must be named `solve`. It must begin with a docstring that has exactly two lines:
    *   The first line must be: "Index: [Index]." using the index from the task header.
    *   The second line must be a succinct, one-sentence description of what the function returns (e.g., "Returns: the total cost of wages and taxes.").

2.  **Function Arguments:** The function arguments must be derived from the 'Question' text. 
    *   Create a distinct argument for every numerical value that is directly stated in the text.
    *   The arguments should be created **in the same order in which they appear in the question**.
    *   **Note:** Some of these arguments may end up not being used in the function body. This is expected. Do not worry about this and leave the unused arguments in the function signature.

3.  **Argument Formatting:** Each argument must include a type-hint (e.g., `int`, `float`) and a default value equal to its value in the 'Question'. You must also add a comment (`#`) next to each argument that quotes or refers to the phrase in the 'Question' it comes from. 

4.  **Function Body:** The body of the function should follow the logic of the provided 'Solution' dict, which contains the step-by-step solution to the problem. The keys of this dict are strings (e.g. `"L1"`, `"L2"`) which refer to the line number, and the values of the dict are the corresponding steps in the solution. 
    * For every relevant line in the 'Solution', you must include a comment in the Python code that indicates the line number (key) from the 'Solution' dict.
    * These comments should be formatted as `#: L<n>`, where `<n>` is the line number from the 'Solution' dict.
    * Immediately follow the comment with the Python statement that performs the calculation.

5.  **Calculator Annotations:** Pay close attention to the calculator annotations (e.g., `[[25*8=200]]`) in the 'Solution' as they reveal the precise mathematical operations to implement. **Note**: Some lines in the solution may not contain calculator annotations, but you should still pay attention to the logic and calculations described in those lines.

6.  **Final Answer:** Store the final answer in a variable named 'answer', and on the same line, add the comment `# FINAL ANSWER`. In the next line, return the 'answer' variable.

7. **No extra output:** Your output should end with the ``` closing the code block. Do not include any additional text, explanations, or comments outside of the code block."""


def build_solution_mapping(
    index: int,
    dataset: Any,
    convert_brackets: bool = True,
):
    """
    Parameters
    ----------
    index : int
        Position of the sample in the loaded dataset.
    dataset : iterable / HuggingFace Dataset
    convert_brackets : bool, default ``True``
        If ``True`` replace every ``<< … >>`` calculator annotation with
        the canonical ``[[ … ]]`` form so downstream code sees a single
        bracket style.

    Returns
    -------
    Dict[str, str]
        Mapping ``{"L1": <first non-empty line>, "L2": <second>, …}``.

    Notes
    -----
    * Blank lines in ``sample["answer"]`` are ignored.
    * The line numbering reflects the *order* in the original solution
      string; there is no semantic grouping beyond that.
    """
    # extract & split solution text
    solution_text = dataset[index]["answer"]
    lines = [ln.strip() for ln in solution_text.splitlines() if ln.strip()]

    # Remove the last line if it matches the '####' answer pattern
    if lines and re.match(r"^####\s*\d+(\.\d+)?$", lines[-1]):
        lines = lines[:-1]

    # optional bracket normalisation
    if convert_brackets:
        angle = re.compile(r"<<([^>]+)>>")
        lines = [angle.sub(r"[[\1]]", ln) for ln in lines]
    # build mapping
    return {f"L{i}": line for i, line in enumerate(lines, 1)}


def get_code_strings(indices: List[int], savepath: str = 'code_examples'):
    """
    Returns a dictionary of code strings (manually created or LLM-generated) for the given indices by importing the corresponding code."""
    code_strings = {}
    for idx in indices:
        module = importlib.import_module(f"{savepath}._{idx}")
        code = inspect.getsource(module.solve)
        code_strings[idx] = code
    return code_strings


def format_prompt_query(
        index: int, 
        code_strings: dict,
        with_code: bool = False
):
    """
    Returns a string with the text for a problem's Index, Question, Solution (as dict), and (if `with_code == True`) the corresponding code.
    """
    sample = gsm8k_train[index] # type: ignore
    question = sample["question"]
    # Use the solution mapping dict instead of raw solution text
    solution_mapping = build_solution_mapping(index, gsm8k_train)
    solution = json.dumps(solution_mapping) # Format as JSON

    out = f"""*Index*: 
{index}

*Question*: 
{question}

*Solution*: 
{solution}

*Code*:"""
    if with_code:
        out += f"""\n```python
{code_strings[index]}
```"""
    return out


def craft_user_prompt(
    index: int,
    example_indices: List[int],
    code_examples: Dict[int, str]
    ):
    """
Generates a complete user prompt for the LLM to generate code. This function assembles the guidelines, few-shot examples, and the final unsolved task into a single string, ready to be sent to an LLM.

Args:
    index: The index of the target problem to generate code for.
    example_indices: A list of indices to use as few-shot examples.
    code_examples: A dictionary mapping example indices to their code strings.

Returns:
    A single string containing the full user prompt.
"""
    # This function assumes a variable `PROMPT_GUIDELINES` exists in its scope.

    # Generate the formatted strings for the few-shot examples
    example_prompts = [
        format_prompt_query(index=idx, 
                             code_strings=code_examples,
                             with_code=True)
        for idx in example_indices
    ]

    # Generate the formatted string for the final task to be completed by the LLM
    task_prompt = format_prompt_query(index=index, code_strings=code_examples)

    # Combine all parts into a single prompt string
    full_prompt = "\n".join([
        PROMPT_GUIDELINES,
        "\n--- EXAMPLES ---\n",
        "\n".join(example_prompts),
        "--- TASK ---\n",
        task_prompt
    ])

    return full_prompt


def call_model_api(
        provider: str, 
        model: str, 
        system_prompt: str, 
        user_prompt: str):
    """
    Calls the appropriate LLM API based on the provider and returns the raw text response.
    
    This function handles special cases for reasoning models like o3-mini that do not
    support the temperature parameter.

    Args:
        provider: The API provider ("google", "anthropic", or "openai").
        model: The specific model name to use.
        system_prompt: The system-level instructions for the model.
        user_prompt: The user-level prompt containing examples and the task.

    Returns:
        The model's generated text content as a string, or None if an error occurs.
    """
    try:
        if provider == "google":
            gemini = genai.GenerativeModel(
                model_name=model,
                system_instruction=system_prompt
            )
            generation_config = genai.types.GenerationConfig(
                temperature=0.1,
                max_output_tokens=4000
            )
            response = gemini.generate_content(
                user_prompt,
                generation_config=generation_config
            )
            return response.text

        elif provider == "anthropic":
            response = anthropic_client.messages.create(
                model=model,
                max_tokens=4000,
                temperature=0.1,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}]
            )
            return response.content[0].text

        elif provider == "openai":
            # Prepare the arguments for the API call
            kwargs = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            }
            
            # Conditionally set parameters based on model type
            if model not in ["o3-mini", "o4-mini"]:
                kwargs["temperature"] = 0.1
                kwargs["max_tokens"] = 4000

            response = openai_client.chat.completions.create(**kwargs)
            return response.choices[0].message.content
        
        else:
            print(f"Unknown provider: {provider}")
            return None
            
    except Exception as e:
        print(f"An API error occurred for {provider} model {model}: {e}")
        return None


def generate_GSM8K_code(
    model_dict: Dict[str, List[str]],
    indices_to_generate: List[int],
    example_indices: List[int],
    system_prompt: str = SYSTEM_PROMPT
):
    """
    Calls multiple LLM APIs, saves the raw output, and logs performance. Also, returns the performance data as a DataFrame for convenience. 

    Args:
        model_dict: Dictionary of providers and their models to test.
        indices_to_generate: List of GSM8K problem indices to generate code for.
        example_indices: List of indices to use as few-shot examples in the prompt.
        system_prompt: The system prompt to send to the models.
    """

    # 1. Initialize performance logging
    performance_data = []
    base_output_dir = 'code_generation_outputs'
    os.makedirs(base_output_dir, exist_ok=True)

    # Loop over each problem you want to solve
    for index in indices_to_generate:
        print(f"\n{'='*20} Starting Generation for Index: {index} {'='*20}")

        # 2. Create the output directory for the current problem index
        problem_dir = os.path.join(base_output_dir, str(index))
        os.makedirs(problem_dir, exist_ok=True)
        print(f"Output directory: {problem_dir}")

        # 3. Create the user prompt once for this problem index
        print("Crafting user prompt...")
        user_prompt = craft_user_prompt(
            index=index,
            example_indices=example_indices,
            code_examples=get_code_strings(example_indices)
        )

        # 4. Loop over each provider and model in your dictionary
        for provider, models in model_dict.items():
            for model_name in models:
                print(f"\n--- Calling {provider.capitalize()} model: {model_name} ---")

                # 5. Call the API and time the request
                start_time = time.time()
                raw_response = call_model_api(provider, model_name, system_prompt, user_prompt)
                end_time = time.time()
                
                time_taken = end_time - start_time
                print(f"  Response received in {time_taken:.2f} seconds.")

                # Log the performance data
                performance_data.append({
                    'provider': provider,
                    'model': model_name,
                    'index': index,
                    'time_taken': time_taken
                })

                # 6. Save the raw response to a file
                if raw_response:
                    output_filename = f'{provider}_{model_name}.txt'
                    output_path = os.path.join(problem_dir, output_filename)
                    try:
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(raw_response)
                        print(f"  Successfully saved raw output to: {output_path}")
                    except IOError as e:
                        print(f"  Error: Failed to write file. Reason: {e}")
                else:
                    print("  No response received. Skipping file save.")

    print(f"\n{'='*20} Generation Complete {'='*20}")

    # 7. Save the performance data to a CSV file at the end
    df = pd.DataFrame(performance_data)
    csv_path = os.path.join(base_output_dir, 'generation_performance.csv')
    df.to_csv(csv_path, index=False)
    print(f"Performance data successfully saved to {csv_path}.")

    return df



# indices = [310, 3822, 7371]

# model_dict = \
# {
#   "anthropic": [
#     "claude-3-5-haiku-20241022"
#   ],
#   "openai": [
#     "o4-mini",
#     "gpt-4.1-mini"
#   ],
#   "google": [
#     "gemini-2.0-flash-thinking-exp",
#     "gemini-2.5-flash-lite-preview-06-17"
#   ]
# }