# Solution Verifier LLM - Project Strategy

## **Project Strategy: A High-Rigor Pipeline for a 'Solution Verifier' LLM**

This document outlines the end-to-end strategy for fine-tuning a Large Language Model (LLM) to detect, classify, and correct errors in natural language mathematical solutions. The strategy is presented in reverse, starting from the final project goal and working backward to justify each component of the data generation and evaluation pipeline.

### 1. Project Goal

The primary objective is to fine-tune a small (<20B parameter) LLM to function as a **Solution Verifier**. At inference time, this model must accept a standalone natural language problem and a corresponding natural language solution as its only inputs. Without any other context or "cheats," it must produce a structured, machine-readable analysis of the solution's validity. This ensures the final model is applicable to the challenging real-world use case of verifying reasoning from raw text.

### 2. Evaluation Framework

To verifiably measure the model's success against this goal, a multi-tiered evaluation framework is required.

* **Tier 1: Classification Performance.** These are fundamental metrics to establish a baseline and measure overall improvement.
  * **Verdict Accuracy:** The model's ability to correctly classify a solution as "Correct" or "Flawed".
  * **Error Type Accuracy:** Conditional on a "Flawed" verdict, the model's ability to correctly select the error category from our predefined taxonomy (e.g., `computational_error`, `incorrect_operation`).
    While necessary, these metrics are insufficient as they do not guarantee genuine understanding; a model could achieve high accuracy by learning superficial patterns.

* **Tier 2: Functional Correctness.** To address the limitations of simple accuracy, we will evaluate the model's reasoning capability via a rigorous proxy: testing if its proposed correction is functionally correct. The resulting metric, the **Correction Success Rate**, is the primary measure of the model's performance. It is calculated via a multi-step pipeline:
    1. **Variable Mapping:** The model will generate a `correction_in_code` string with its own invented variable names. Our evaluation script will programmatically map these names to the ground-truth variables in our `f_flawed` function by using semantic similarity (SBERT embeddings) on the variables from the relevant line of code.
    2. **Correction Normalization:** Using this mapping, the script will generate a **normalized correction** string that uses the canonical variable names from `f_flawed`.
    3. **Consensus-Based Repair:** We will prompt three powerful, independent LLMs with `f_flawed` and the normalized correction, instructing them to produce a repaired function. This consensus approach mitigates the risk of any single judge model failing to interpret the instruction.
    4. **Programmatic Fuzzing:** Each of the three resulting `f_repaired` functions will be programmatically fuzz-tested for functional equivalence against the original `f_oracle`.
    5. **Metric Calculation:** The model's correction is deemed "successful" if at least two of the three repair attempts result in a functionally correct function.

### 3. Required Model Output Structure

The Tier 2 evaluation framework dictates that the model must produce a highly structured JSON object, not just natural language. The fine-tuning target is therefore a JSON containing specific, machine-parsable fields that enable the programmatic checks.

```json
{
  "verdict": "Flawed",
  "error_details": {
    "error_type": "incorrect_operation",
    "erroneous_line_number": "L1",
    "explanation": "A natural language explanation of the error.",
    "error_in_code": "cost_of_supplies = number_of_boxes + price_per_box",
    "correction_in_code": "cost_of_supplies = number_of_boxes * price_per_box"
  }
}
```

The fields `erroneous_line_number`, `error_in_code`, and `correction_in_code` are essential. They provide the necessary hooks for the evaluation script to locate the error, map the model's invented symbols, and generate the normalized correction for the consensus-based repair step.

### 4. Fine-Tuning Strategy and Dataset

To train the model to produce this specific JSON output, we will use Supervised Fine-Tuning (SFT).

* **Dataset Structure:** The training data will consist of `(input, target)` pairs.
  * **Input:** A string containing only the `problem_text` and the `flawed_nl_solution`. No symbolic context is provided, forcing the model to learn to generate its own symbols from the raw problem text.
  * **Target:** The complete JSON object described in Section 3.

* **The SFT Mechanism:** The fine-tuning process relies on a standard **next-token prediction** task with a **cross-entropy loss**.
    1. The target JSON object is serialized into a single string and then tokenized.
    2. For each token in this target sequence, the model predicts a probability distribution over the vocabulary. The loss is calculated between this prediction and the ground-truth token.
    3. This loss is backpropagated to update the model weights. This happens for *every single token*, forcing the model to learn not only the semantic content but also the rigid syntax of the JSON structure.
    4. To consistently minimize this loss across a large and diverse dataset, simple memorization is an inefficient strategy. The model is incentivized to generalize by building an internal, abstract representation of the reasoning process required to get from the input text to the target JSON.

### 5. Data Generation Strategy via Error Injection

The creation of the high-quality SFT dataset from Section 4 is the central data engineering challenge. To ensure perfect labels, we will synthesize the data rather than relying on LLM annotation.

* **Core Strategy:** The process begins with a validated `f_oracle`. An error is programmatically injected into its Abstract Syntax Tree (AST) to create `f_flawed`. This programmatic action provides all the metadata required to instantly and perfectly generate the `target_json` label. The tentative error categories and injection methods are as follows:
  * **`computational_error`:** The result of a numeric calculation is altered. In the AST, this involves finding an assignment node and replacing the right-hand side with a new constant value (e.g., `total = 5 * 10` becomes `total = 51`).
  * **`incorrect_operation`:** A mathematical operator is swapped. In the AST, this means replacing an operator node (e.g., `ast.Mult` becomes `ast.Add`).
  * **`incorrect_operand`:** A variable in a calculation is replaced with another variable from the same scope. This involves finding and replacing an `ast.Name` node with a different valid variable name.
  * **`skipped_step`:** A necessary line of code is removed. This involves deleting an entire assignment node from the AST and handling any subsequent `NameError` by replacing later references to the deleted variable with a plausible (but incorrect) value.

* **Anticipated Difficulties:** After creating `f_flawed` and its corresponding `target_json`, the most difficult step is generating the `flawed_nl_solution`. This will require prompting a powerful LLM to write a plausible, human-like solution that adheres to the flawed logic of `f_flawed`, constrained by its incorrect intermediate values. The primary challenges will be ensuring the generated text accurately reflects the intended logical flaw without introducing other unintended errors, and maintaining a natural tone. This generation-and-validation loop for the natural language component is the most significant remaining challenge in the data pipeline.

### 6. Foundational Prerequisite: The "Oracle Factory"

The entire strategy above—from evaluation to data generation—is predicated on the existence of a high-confidence, ground-truth `f_oracle` for each problem. This is why the first and most complex part of our project is the "Oracle Factory" pipeline. It is an automated workflow that creates and validates the necessary ground-truth functions.

* **1. Code Generation:** For each GSM8K problem, asynchronous API calls are made to multiple, independent LLMs (e.g., from OpenAI, Anthropic, Google). Each model is prompted to convert the natural language problem and solution into a single, well-structured Python function named `solve`.

* **2. Validation and Consensus Pipeline:** The generated Python files for a given problem are then subjected to a rigorous, multi-stage validation process to find a robust consensus.
  * **UT-1 (Parse & Pre-filter):** All files are parsed to extract the function signature, including argument names, types, default values, and comments. Any function that fails to produce the correct final answer from the GSM8K dataset using its default arguments is immediately discarded.
  * **UT-2 (Pairwise Alignment):** For every surviving pair of functions, the script finds the best possible argument alignment using an efficient "bucket and match" strategy. Arguments are first grouped into "buckets" by their `(type, default_value)`. A semantic comparison using SBERT cosine similarity is then performed only on arguments within matching buckets, robustly handling differences in naming and ordering.
  * **UT-3 (Pairwise Fuzzing):** Each successfully aligned pair is then tested for functional equivalence using the `hypothesis` library. This employs a "Fuzz Aligned, Freeze Unaligned" strategy, where aligned arguments are fuzzed with a wide range of values while unaligned arguments are held constant at their defaults. A pair passes if their outputs remain identical across all fuzzed inputs, proving their underlying mathematical logic is identical.

* **3. Final Confidence Score:** The results of the validation pipeline are synthesized into a final `ConfidenceScore` for the problem. This score provides a single, quantifiable measure of our confidence in the generated oracles. It is computed as follows:
    1. A graph is constructed where functions are nodes and an edge exists between any pair that passed the fuzzing test. The script identifies the largest fully connected subgraph (the **consensus clique**).
    2. For each validated pair in the clique, a `PairwiseQualityScore` is calculated as a weighted average of its **Alignment Ratio** (proportion of aligned arguments) and its **Semantic Strength** (average SBERT similarity of aligned argument names/comments).
    3. The final `ConfidenceScore` is the average `PairwiseQualityScore` of all pairs within the best clique, amplified by a **Consensus Bonus** multiplier that increases with the size of the clique (e.g., x1.1 for 3 models, x1.2 for 4 models).

Only a problem that achieves a high `ConfidenceScore` will yield a canonical `f_oracle` trustworthy enough to serve as the foundation for the entire downstream error injection and model training workflow.