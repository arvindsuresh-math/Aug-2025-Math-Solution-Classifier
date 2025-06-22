# Project Pipeline: Generating Classified Math Problems

This document outlines a suggested pipeline for generating a dataset of classified mathematical word problems adapted from the GSM8K dataset. The primary goal is to produce a high-quality dataset for fine-tuning a Large Language Model (LLM) to classify problems into one of three categories:
*   **Class 1 (Solvable):** The original, well-posed problem with a unique solution.
*   **Class 0 (Contradictory):** A modified problem containing conflicting information that makes a solution impossible.
*   **Class 2 (Underspecified):** A modified problem with insufficient information, leading to multiple or infinite solutions.

The basic strategy is to prompt an LLM to inject errors into problems so as to generate labelled samples in classes 0 and 2. The difficulty lies in ensuring the correctness of the generated samples. Preliminary experiments in directly prompting an LLM to generate such problems had mixed success. Some outputs being correct (i.e. they correctly injected an error to place the problem in the desired class), but many were not. More importantly, it was not at clear how to ensure that the generated problems were correct, or at least that they were correct with high confidence. One idea (already present in the literature) is to use an ensemble of LLMs to generate the same problem, and then use a voting strategy to select the most likely correct output. However, this approach is expensive in terms of API calls and latency, and it still does not guarantee correctness. 

The main aim of the pipeline below is to modify the naive prompting strategy to (try to) ensure that the generated problems are correct with high confidence. The main idea is to use LLMs to first convert the GSM8K problems and solutions (both natural language) into structured Python functions that encapsulate the problem's logic and numerical quantities. The reason for doing this is as follows:
    1. Preliminary experiments show that LLMs are really good at converting natural language problems into structured Python functions, when provided with strict guidelines and a few examples. Several LLMs with low API cost and latency (e.g. `4.1-mini`, `claude_3-5-haiku`, `gemini-flash-2.5`) were able to generate correct functions for some of the longest GSM8K questions. 
    2. Unlike in the natural language case, it turns out that it is easier to try to convince ourselves that the generated 
    
    I feel somewhat confident saying "correct functions" because of the following checks conducted on the generated functions:
        *   **Parse & Pre-filter:** A robust, regex-based parser is used to check the syntax of the generated code and execute it with default arguments to ensure it produces the correct answer for the original problem.
        *   **Pairwise Alignment:** A semantic comparison is performed on the function parameters to ensure they are aligned in meaning, even if their names or order differ.
        *   **Pairwise Fuzzing:** A property-based fuzz test is conducted to ensure that pairs of functions are functionally equivalent under known constraints.


*   **Formalization:** Convert GSM8K problems into structured Python functions that encapsulate the problem's logic and numerical quantities. This will be done by 3 low cost LLMs (e.g. `4.1-mini`, `claude_3-5-haiku`, `gemini-flash-2.5`) that are prompted to generate a single Python function named `solve()`. The function will take the problem's numerical quantities as typed arguments with default values and descriptive comments, and implement the solution logic in the function body.
*   **Validation:** Use a multi-unit test approach to verify the correctness and consistency of the generated functions. This involves parsing, pairwise alignment, and fuzz testing to ensure functional equivalence.
*   **Consensus Finding:** Identify a consensus group of validated functions and select a single "canonical" function to represent the problem.


*   **Error Injection:** Programmatically modify the canonical function to create flawed problem variants, generating labeled training examples for fine-tuning.

---

## The Four Stages of the Pipeline

The process is divided into four main stages:

### Stage 0: Code Generation (Problem Formalization)

The foundation of the pipeline is the conversion of unstructured, natural language math problems into structured, machine-readable Python functions.

1.  **Prompting:** Multiple independent LLMs (e.g., from OpenAI, Google, Anthropic) are given a GSM8K problem and its natural language solution. They are prompted with strict guidelines and few-shot examples to convert the problem into a single Python function named `solve()`.
2.  **Formalization:** The generated function must encapsulate the problem's numerical quantities as typed arguments with default values and descriptive comments. The solution's logic is implemented in the function body. This "formalization" creates a computable representation of the problem.

### Stage 1: Validation and Consensus Finding

This is the most critical stage, designed to automatically verify the correctness and consistency of the LLM-generated code. It uses a multi-unit test (`UT`) approach to find a consensus among the different model outputs.

*   **UT-1: Parse & Pre-filter**
    *   **Action:** All generated Python files for a problem are parsed using a robust, regex-based approach. Each function is executed with its default arguments.
    *   **Goal:** To perform a basic sanity check, filtering out any models that produced syntactically incorrect code or whose logic failed to yield the correct answer for the original problem.

*   **UT-2: Pairwise Alignment**
    *   **Action:** Every possible pair of the surviving models is compared. The script uses a "bucket and match" strategy, first grouping function arguments by `(type, default_value)`. Only within these matching buckets does it perform a semantic comparison using a Sentence-BERT (SBERT) model on the combined text of the argument's `name` and `comment`.
    *   **Goal:** To find a robust semantic alignment between the parameters of two functions, without being brittle about the exact argument names or their order in the function signature.

*   **UT-3: Pairwise Fuzzing**
    *   **Action:** For each successfully aligned pair from UT-2, a property-based fuzz test is conducted using the "Fuzz Aligned, Freeze Unaligned" strategy. Random values are generated for the aligned arguments while unaligned arguments are held constant at their default values. The outputs of both functions are asserted to be equal.
    *   **Goal:** To rigorously prove that the two functions are **functionally equivalent** under known constraints, ensuring their underlying mathematical logic is identical.

*   **Scoring & Reporting**
    *   **Action:** Each validated pair is given a `PairwiseQualityScore`. The system then identifies the largest "clique" (group of models that all mutually passed validation against each other) and calculates a final **Confidence Score** based on the average quality within the clique, boosted by a bonus for the size of the consensus.
    *   **Goal:** To produce a single, quantitative metric (0.0 to 1.0+) that represents our confidence in the generated formalization for that problem.

### Stage 2: Canonical Function Selection

With a validated group of functions, we select one to be the "canonical" representation for the final stage.

1.  **Selection:** From the highest-scoring consensus clique identified in Stage 1, a single `solve()` function is chosen.
2.  **Criteria:** The choice can be based on which function has the most parameters (i.e., is the most general), or it can be a random selection from the validated group.
3.  **Goal:** To have a single, high-confidence, machine-readable artifact that will serve as the basis for error injection.

### Stage 3: Programmatic Error Injection

This final stage uses the canonical `solve()` function to create the flawed problem variants.

1.  **Analysis:** The canonical function's parameters are analyzed.
2.  **Modification:** The function's default arguments are programmatically altered to create logical flaws. The corresponding numerical values in the original natural language problem text are updated to match.
    *   To create a **Class 0 (Contradictory)** problem, argument values are changed to create a logical impossibility. For example, if the original problem has `apples = 5` and `oranges = 3` for a `total_fruit = 8`, the arguments might be changed to `apples = 6` and `oranges = 3` while the text still references a total of 8.
    *   To create a **Class 2 (Underspecified)** problem, a necessary argument is removed from the function signature, and the corresponding sentence providing that value is removed from the problem text.
3.  **Output:** The process outputs a labeled training example consisting of the `(modified_problem_text, error_class_label)` pair, ready to be used for fine-tuning.