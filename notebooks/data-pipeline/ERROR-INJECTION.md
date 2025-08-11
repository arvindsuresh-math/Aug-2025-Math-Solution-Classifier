# The Error Injection Pipeline

The foundation of a reliable verification model is a high-quality training dataset that includes a wide variety of realistic errors. Manually creating thousands of flawed examples is impractical. Instead, we developed a programmatic error injection pipeline that uses the `Formalization Templates` to generate a large and diverse set of flawed solutions.

## Core Strategy: Modifying the Abstract Syntax Tree (AST)

The key to our approach is treating the Python `function_code` from our templates not as text, but as a structured **Abstract Syntax Tree (AST)**. An AST is a tree representation of the code's structure, where each node represents an operation, a variable, or a value.

Our pipeline works by:

1. Parsing the correct `function_code` into its AST.
2. Programmatically modifying this tree to introduce a specific, targeted error.
3. Converting the modified AST back into executable Python code.
4. Running the new, flawed code to generate a "flawed trace" of variable values.
5. Using this flawed trace and the original `logical_steps` to reconstruct a new, flawed solution in natural language.

This AST-based method gives us precise control and allows us to create errors that are subtle and propagate realistically through the entire solution.

## 1. Computational Error Generation

This part of the pipeline is fully automated and designed to produce solutions with verifiable calculation mistakes.

The process is context-aware. We don't just add random noise to numbers. Instead, for each variable calculated in the `function_code`, the system first determines which types of errors are plausible. The logic for determining **allowable errors** depends on the variable's data type (e.g., integer, float, or fraction) and the mathematical operation used to compute it.

For example, a "digit transposition" error is only applied to integers with at least two different digits, while a "decimal shift" error is only applied to floating-point numbers.

The primary subtypes of computational errors we generate include:

* **Off-by-N Error:** A minor miscalculation where the result is off by a small integer (e.g., `12 + 5 = 18`).
* **Off-by-Factor-of-10 Error:** A decimal placement mistake, typically dropping or adding a zero (e.g., `50 * 10 = 50`).
* **Digit Transposition Error:** Swapping two adjacent digits, a common human typo (e.g., `125` becomes `152`).
* **Stem Off-by-N Error:** A miscalculation affecting the "stem" of a number ending in zero (e.g., `120 + 50 = 180`).
* **Decimal Shift Error:** Misplacing the decimal point in a float by a factor of 10.
* **Fraction Reciprocal Error:** Swapping the numerator and denominator of a fraction.
* **Off-by-One in Fraction Part:** An error in either the numerator or denominator of a fraction.
* **Multiplication by Reciprocal:** Incorrectly multiplying by a fraction's reciprocal (e.g., multiplying by `4/3` instead of `3/4`).

## 2. Conceptual Error Generation

Conceptual errors are mistakes in logic or reasoning, not just calculation. Generating them is more complex, as there are more possibilities and a higher risk of creating a solution that is nonsensical.

The process for conceptual errors focuses on **discovering mutation opportunities** within the AST. The system analyzes the `function_code` to find places where a logical mistake could plausibly be made.

The primary subtypes of conceptual errors we generate include:

* **Operator Swap:** Using the wrong mathematical operator (e.g., using `+` when subtraction was required).
* **Incomplete Calculation:** Omitting a necessary term from a calculation (e.g., calculating `price1 + price2` when the total should have been `price1 + price2 + tax`).
* **Incorrect Operand:** Using a logically incorrect variable in a calculation, even if it's numerically plausible (e.g., using a `subtotal` value again instead of the `total_cost_with_tax`).
* **Input Misrepresentation:** Misusing a value from the original question text.
* **Incorrect Final Answer Selection:** Reporting an intermediate result as the final answer instead of the correct final value.

### Human-in-the-Loop Validation for Conceptual Errors

While the computational error pipeline is fully automated, conceptual errors are more subtle. A programmatic change can sometimes result in a solution that is confusing, nonsensical, or simply not a realistic mistake a human would make.

Therefore, the conceptual error pipeline generates plausible **candidates** that are refined and verified through a final human-in-the-loop (HITL) process. This ensures the logical flaws in our final training data are both high-quality and natural. This process involves two main stages:

#### 1. Candidate Sampling and Shortlisting

The generation process produces over 30,000 potential error candidates. Manually reviewing all of them would be inefficient. To create a manageable and diverse validation task, we programmatically sample a shortlist of the most promising candidates.

The sampling logic is designed to ensure a balanced representation across different types of problems and error locations, rather than just selecting randomly. We use a **stratified sampling** approach based on two key dimensions:

1. **Problem Complexity (Tier):** The five-tier system used during template generation (from simple integer arithmetic to complex algebra).
2. **Relative Error Position (Position Bin):** Whether the error occurs **early**, in the **middle**, or **late** in the solution's step-by-step logic.

The script first filters the candidate pool to only include those generated from high-quality templates that passed our most rigorous validation checks. Then, for each mutation type (e.g., `operator_swap`, `incorrect_operand`), it samples a target number of candidates, ensuring they are distributed across the various `(tier, position_bin)` combinations. This method prevents over-sampling from common problem types and guarantees that our validation effort covers a wide range of scenarios.

Finally, the ~2,000 shortlisted candidates are distributed evenly among the project's team members, with each person receiving a personal `validation_catalog.csv` file to track their progress.

#### 2. The Validation Application

To make the validation process as efficient as possible, we built a simple web application using Streamlit. The tool is launched from the command line and is pointed at a specific validator's catalog file.

The interface is designed for rapid, side-by-side comparison:

* **UI Layout:** The screen displays the correct solution on the left and the programmatically generated flawed solution on the right.
* **Editable Fields:** While the correct solution is locked, every line of the flawed solution is presented in an editable text box. This allows the validator to make minor wording changes to improve the natural language flow of the flawed answer. The generated `explanation` and the flagged `erroneous_line_number` are also editable.
* **Decision and Persistence:** For each candidate, the validator makes one of three choices:
  * **✅ Accept:** The candidate is deemed a high-quality, realistic error. The final (and potentially edited) version of the flawed solution and its metadata are saved to a new JSON file in a separate directory (`conceptual-errors-accepted`).
  * **❌ Reject:** The candidate is deemed unrealistic, nonsensical, or unfixable.
  * **⏭️ Skip:** The validator can skip the candidate and return to it later.
* **State Management:** Every decision is instantly saved to the validator's personal `.csv` catalog. This makes the process robust, allowing a user to stop and resume their session at any time without losing work.

This HITL pipeline combines the scalability of programmatic generation with the nuance of human judgment, resulting in a final, verified dataset of conceptual errors that is clean, diverse, and ready for model training.
