# The Error Injection Pipeline

The foundation of a reliable verification model is a high-quality training dataset that includes a wide variety of realistic errors. Manually creating thousands of flawed examples is impractical. Instead, we developed a programmatic error injection pipeline that uses the `Formalization Templates` to generate a large and diverse set of flawed solutions.

## Core Strategy: Modifying the Abstract Syntax Tree (AST)

The key to our approach is treating the Python `function_code` from our templates not as text, but as a structured **Abstract Syntax Tree (AST)**. An AST is a tree representation of the code's structure, where each node represents an operation, a variable, or a value.

Our pipeline works by:
1.  Parsing the correct `function_code` into its AST.
2.  Programmatically modifying this tree to introduce a specific, targeted error.
3.  Converting the modified AST back into executable Python code.
4.  Running the new, flawed code to generate a "flawed trace" of variable values.
5.  Using this flawed trace and the original `logical_steps` to reconstruct a new, flawed solution in natural language.

This AST-based method gives us precise control and allows us to create errors that are subtle and propagate realistically through the entire solution.

## 1. Computational Error Generation

This part of the pipeline is fully automated and designed to produce solutions with verifiable calculation mistakes.

The process is context-aware. We don't just add random noise to numbers. Instead, for each variable calculated in the `function_code`, the system first determines which types of errors are plausible. The logic for determining **allowable errors** depends on the variable's data type (e.g., integer, float, or fraction) and the mathematical operation used to compute it.

For example, a "digit transposition" error is only applied to integers with at least two different digits, while a "decimal shift" error is only applied to floating-point numbers.

The primary subtypes of computational errors we generate include:

*   **Off-by-N Error:** A minor miscalculation where the result is off by a small integer (e.g., `12 + 5 = 18`).
*   **Off-by-Factor-of-10 Error:** A decimal placement mistake, typically dropping or adding a zero (e.g., `50 * 10 = 50`).
*   **Digit Transposition Error:** Swapping two adjacent digits, a common human typo (e.g., `125` becomes `152`).
*   **Stem Off-by-N Error:** A miscalculation affecting the "stem" of a number ending in zero (e.g., `120 + 50 = 180`).
*   **Decimal Shift Error:** Misplacing the decimal point in a float by a factor of 10.
*   **Fraction Reciprocal Error:** Swapping the numerator and denominator of a fraction.
*   **Off-by-One in Fraction Part:** An error in either the numerator or denominator of a fraction.
*   **Multiplication by Reciprocal:** Incorrectly multiplying by a fraction's reciprocal (e.g., multiplying by `4/3` instead of `3/4`).

## 2. Conceptual Error Generation

Conceptual errors are mistakes in logic or reasoning, not just calculation. Generating them is more complex, as there are more possibilities and a higher risk of creating a solution that is nonsensical.

The process for conceptual errors focuses on **discovering mutation opportunities** within the AST. The system analyzes the `function_code` to find places where a logical mistake could plausibly be made.

The primary subtypes of conceptual errors we generate include:

*   **Operator Swap:** Using the wrong mathematical operator (e.g., using `+` when subtraction was required).
*   **Incomplete Calculation:** Omitting a necessary term from a calculation (e.g., calculating `price1 + price2` when the total should have been `price1 + price2 + tax`).
*   **Incorrect Operand:** Using a logically incorrect variable in a calculation, even if it's numerically plausible (e.g., using a `subtotal` value again instead of the `total_cost_with_tax`).
*   **Input Misrepresentation:** Misusing a value from the original question text.
*   **Incorrect Final Answer Selection:** Reporting an intermediate result as the final answer instead of the correct final value.

### Human-in-the-Loop Validation

While the computational error pipeline is fully automated, conceptual errors are more subtle. A programmatic change can sometimes result in a solution that is confusing or nonsensical.

Therefore, the conceptual error pipeline generates **candidates**. Each candidate includes the original correct solution, the proposed flawed solution, and a detailed explanation of the mutation that was applied. These candidates are then passed to a final, manual review stage where a human annotator can quickly accept, reject, or edit them. This ensures the logical flaws in our training data are both realistic and understandable.