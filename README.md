# Solution Verifier LLM - Project Strategy

## **Project Strategy: A High-Rigor Pipeline for a 'Solution Verifier' LLM**

This document outlines the end-to-end strategy for fine-tuning a Large Language Model (LLM) to detect, classify, and correct errors in natural language mathematical solutions. The strategy is presented in reverse, starting from the final project goal and working backward to justify each component of the data generation and evaluation pipeline.

### 1. Project Goal

The primary objective is to fine-tune a small (<20B parameter) LLM to function as a **Solution Verifier**. At inference time, this model must accept a standalone natural language problem and a corresponding natural language solution as its only inputs. Without any other context or "cheats," it must produce a structured, machine-readable analysis of the solution's validity. This ensures the final model is applicable to the challenging real-world use case of verifying reasoning from raw text.

### 2. Evaluation Metrics

To verifiably measure the model's success against this goal, the evaluation will focus on classification performance.

*   **Verdict Accuracy:** The model's ability to correctly classify a solution as "Correct" or "Flawed".
*   **Error Type Accuracy:** Conditional on a "Flawed" verdict, the model's ability to correctly select the error category from our predefined taxonomy (e.g., `computational_error`, `incorrect_world_knowledge`).

While necessary, these metrics are insufficient as they do not guarantee genuine understanding; a model could achieve high accuracy by learning superficial patterns. Future work may re-introduce more rigorous functional testing, but for now, these classification metrics are the primary measure of performance.

### 3. Required Model Output Structure

To enable programmatic evaluation, the model must produce a structured JSON object. The fine-tuning target is therefore a JSON containing specific, machine-parsable fields.

```json
{
  "verdict": "Flawed",
  "error_details": {
    "error_type": "incorrect_operation",
    "erroneous_line_number": "L1",
    "explanation": "A natural language explanation of the error."
  }
}
```

The fields `verdict`, `error_type`, and `erroneous_line_number` provide the necessary data to calculate the core evaluation metrics.

### 4. Fine-Tuning Strategy and Dataset

To train the model to produce this specific JSON output, we will use Supervised Fine-Tuning (SFT).

*   **Dataset Structure:** The training data will consist of `(input, target)` pairs.
    *   **Input:** A string containing only the `problem_text` and the `flawed_nl_solution`. No symbolic context is provided.
    *   **Target:** The complete JSON object described in Section 3.

*   **The SFT Mechanism:** The fine-tuning process relies on a standard **next-token prediction** task with a **cross-entropy loss**.
    1.  The target JSON object is serialized into a single string and then tokenized.
    2.  For each token in this target sequence, the model predicts a probability distribution over the vocabulary. The loss is calculated between this prediction and the ground-truth token.
    3.  This loss is backpropagated to update the model weights. This happens for *every single token*, forcing the model to learn not only the semantic content but also the rigid syntax of the JSON structure.
    4.  To consistently minimize this loss across a large and diverse dataset, simple memorization is an inefficient strategy. The model is incentivized to generalize by building an internal, abstract representation of the reasoning process required to get from the input text to the target JSON.

### 5. Data Generation via Trace-Based Error Injection

The creation of the high-quality SFT dataset is the central data engineering challenge. To ensure perfect labels, we will synthesize the data.

*   **Core Strategy:** The process begins with a validated `function_code` from a Formalization Manifest. This code is not executed directly to create a flawed version. Instead, it is parsed to create a **dependency graph** and a correct **evaluation trace**—a map of all variables to their correct values. An error is injected by altering a single value in this trace. The change is then propagated through the dependency graph to update all downstream values, resulting in a **flawed evaluation trace**. This flawed trace provides the values needed to generate the `flawed_nl_solution` and the `target_json` label.

*   **Error Categories:**
    *   **`computational_error`:** The result of a numeric calculation (i.e., an `output_variable`) is altered in the trace, and the error is propagated.
    *   **`skipped_step`:** For the natural language solution, this is the most straightforward to generate, as it simply requires removing a line from the original solution.
    *   **`conceptual_error`:** This includes any error that does not fall into the above categories, such as using an incorrect operation or incorrect operands. For now, the plan is to generate these manually, and time permitting, we will explore programmatic generation methods. (Although, one potential simple change that can be made programmatically is to inject "incorrect world knowledge" errors by changing the value of a variable in the `WK_inputs` list.)

*   **Anticipated Difficulties:** After creating the flawed evaluation trace, the most difficult step is generating a plausible `flawed_nl_solution` by substituting the flawed values into the `solution_line_template`s. The primary challenge is ensuring the generated text accurately reflects the intended logical flaw without introducing other unintended errors and maintaining a natural tone.

### 6. Foundational Prerequisite: The "Formalization Manifest"

The entire strategy above is predicated on the existence of a high-confidence, ground-truth manifest for each problem. The `function_code` within the manifest serves as a verifiable blueprint for the solution's logic, enabling the creation of a precise evaluation trace.

The manifest will contain the following components:
```json
{
  "function_code": "A single string containing a complete, self-contained Python function that constitutes an end-to-end formalization of the solution.",
  "logical_steps": [
    {
      "line_number": "The line number from the original solution (e.g., 'L1', 'L2').",
      "question_inputs": "A list of variable names extracted from the question text, used for the first time in this step.",
      "WK_inputs": "A list of variable names from 'world knowledge' (e.g., minutes_per_hour), used for the first time in this step.",
      "output_variable": "The name of the variable being assigned as the result of the main computation in this step.",
      "solution_line_template": "The complete original line from the solution, including the calculator annotation, with all computational numbers replaced by `{variable_name}` placeholders."
    }
  ]
}
```

Here's a brief explanation of each component:

1.  **function_code:** This is the complete Python function that implements the solution. It should be a self-contained function `def solve()` that can be executed independently. Its primary purpose in this pipeline is to serve as a blueprint for generating the evaluation trace.
2.  **logical_steps:** This is a list of dictionaries, each representing a logical step in the solution process. Each step includes the following:

    *   `line_number`: The line number from the original solution.
    *   `question_inputs`: A list of variable names whose values are stated in or can be directly extracted from the `question` text. These are defined for the first time in this step.
    *   `WK_inputs`: A list of variable names whose values come from common-sense "world knowledge" (e.g. `minutes_per_hour = 60`).
    *   `output_variable`: The name of the variable that holds the result of the main computation in this step.
    *   `solution_line_template`: The complete original line from the solution, with all computational numbers replaced by `{variable_name}` placeholders. This allows for a direct mapping between the logical steps and the original solution text, facilitating the generation of the `flawed_nl_solution`.

The formalization manifests will be generated by making API calls to powerful LLMs, guided by detailed instructions and few-shot examples.


#### Saving this here so it doesn't get lost:

tier1_examples = [4, 1372, 3946, 4258, 4764, 6126]
tier2_examples = [310, 2300, 2401, 2918, 4215, 4822]
tier3_examples =  [5, 72, 964, 2332, 2422, 3592, 3822, 4746, 5531]
tier4_examples = [1, 672, 3847, 4847, 5040, 6216]

tier1_final = [3946, 4258, 6126]
tier2_final = [2401, 2918, 4822]
tier3_final = [5, 964, 2422, 3822]
tier4_final = [3847, 4847, 5040, 7037]