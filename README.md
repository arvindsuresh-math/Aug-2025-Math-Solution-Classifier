# Solution Verifier LLM - Project Strategy

## **Project Strategy: A High-Rigor Pipeline for a 'Solution Verifier' LLM**

This document outlines the end-to-end strategy for fine-tuning a Large Language Model (LLM) to detect, classify, and correct errors in natural language mathematical solutions. The strategy is presented in reverse, starting from the final project goal and working backward to justify each component of the data generation and evaluation pipeline.

### 1. Project Goal

The primary objective is to fine-tune a small (<20B parameter) LLM to function as a **Solution Verifier**. At inference time, this model must accept a standalone natural language problem and a corresponding natural language solution as its only inputs. Without any other context or "cheats," it must produce a structured, machine-readable analysis of the solution's validity. This ensures the final model is applicable to the challenging real-world use case of verifying reasoning from raw text.

### 2. Evaluation Metrics

To verifiably measure the model's success against this goal, the evaluation will focus on classification performance.

* **Verdict Accuracy:** The model's ability to correctly classify a solution as "Correct" or "Flawed".
* **Error Type Accuracy:** Conditional on a "Flawed" verdict, the model's ability to correctly select the error category from our predefined taxonomy (e.g., `computational_error`, `incorrect_world_knowledge`).

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

* **Dataset Structure:** The training data will consist of `(input, target)` pairs.
  * **Input:** A string containing only the `problem_text` and the `flawed_nl_solution`. No symbolic context is provided.
  * **Target:** The complete JSON object described in Section 3.

* **The SFT Mechanism:** The fine-tuning process relies on a standard **next-token prediction** task with a **cross-entropy loss**.
    1. The target JSON object is serialized into a single string and then tokenized.
    2. For each token in this target sequence, the model predicts a probability distribution over the vocabulary. The loss is calculated between this prediction and the ground-truth token.
    3. This loss is backpropagated to update the model weights. This happens for *every single token*, forcing the model to learn not only the semantic content but also the rigid syntax of the JSON structure.
    4. To consistently minimize this loss across a large and diverse dataset, simple memorization is an inefficient strategy. The model is incentivized to generalize by building an internal, abstract representation of the reasoning process required to get from the input text to the target JSON.

### 5. Data Generation via Trace-Based Error Injection

The creation of the high-quality SFT dataset is the central data engineering challenge. To ensure perfect labels, we will synthesize the data.

* **Core Strategy:** The process begins with a validated `function_code` from a Formalization Template. This code is not executed directly to create a flawed version. Instead, it is parsed to create a **dependency graph** and a correct **evaluation trace**—a map of all variables to their correct values. An error is injected by altering a single value in this trace. The change is then propagated through the dependency graph to update all downstream values, resulting in a **flawed evaluation trace**. This flawed trace provides the values needed to generate the `flawed_nl_solution` and the `target_json` label.

* **Error Categories:**
  * **`computational_error`:** The result of a numeric calculation (i.e., an `output_variable`) is altered in the trace, and the error is propagated.
  * **`skipped_step`:** For the natural language solution, this is the most straightforward to generate, as it simply requires removing a line from the original solution.
  * **`conceptual_error`:** This includes any error that does not fall into the above categories, such as using an incorrect operation or incorrect operands. For now, the plan is to generate these manually, and time permitting, we will explore programmatic generation methods. (Although, one potential simple change that can be made programmatically is to inject "incorrect world knowledge" errors by changing the value of a variable in the `WK_inputs` list.)

* **Anticipated Difficulties:** After creating the flawed evaluation trace, the most difficult step is generating a plausible `flawed_nl_solution` by substituting the flawed values into the `solution_line_template`s. The primary challenge is ensuring the generated text accurately reflects the intended logical flaw without introducing other unintended errors and maintaining a natural tone.

### 6. Foundational Prerequisite: The "Formalization Template"

The entire strategy above is predicated on the existence of a high-confidence, ground-truth template for each problem. The `function_code` within the template serves as a verifiable blueprint for the solution's logic, enabling the creation of a precise evaluation trace.

The template will contain the following components:
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

1. **function_code:** This is the complete Python function that implements the solution. It should be a self-contained function `def solve()` that can be executed independently. Its primary purpose in this pipeline is to serve as a blueprint for generating the evaluation trace.
2. **logical_steps:** This is a list of dictionaries, each representing a logical step in the solution process. Each step includes the following:

    * `line_number`: The line number from the original solution.
    * `question_inputs`: A list of variable names whose values are stated in or can be directly extracted from the `question` text. These are defined for the first time in this step.
    * `WK_inputs`: A list of variable names whose values come from common-sense "world knowledge" (e.g. `minutes_per_hour = 60`).
    * `output_variable`: The name of the variable that holds the result of the main computation in this step.
    * `solution_line_template`: The complete original line from the solution, with all computational numbers replaced by `{variable_name}` placeholders. This allows for a direct mapping between the logical steps and the original solution text, facilitating the generation of the `flawed_nl_solution`.

The Formalization Templates will be generated by making API calls to powerful LLMs, guided by detailed instructions and few-shot examples.


#### Saving this here so it doesn't get lost:

tier1_examples = [4, 1372, 3946, 4258, 4764, 6126]
tier2_examples = [310, 2300, 2401, 2918, 4215, 4822]
tier3_examples =  [5, 72, 964, 2332, 2422, 3592, 3822, 4746, 5531]
tier4_examples = [1, 672, 3847, 4847, 5040, 6216]

tier1_final = [3946, 4258, 6126]
tier2_final = [2401, 2918, 4822]
tier3_final = [5, 964, 2422, 3822]
tier4_final = [3847, 4847, 5040, 7037]


###$ Error generation directories:

1. Arvind - 'data/computational-errors-generated'
      (currently done: 0-2999 except for symbolic problems)

2. Ling - 'data/gsm8k_1500_1999_conceptual'
      (currently done: 'gsm8k_1500_1599_conceptual_errors.json')

3. Mauro - '/data/manually_gen_incorrect_answers_gsm8k'
      (currently done: 500-999)

4. Yewei - 'yewei/gsm8k_data'
      (currently done: 1000-1499)

5. Ali - 'GSM8_Edited'
      (currently done: 0-500)


#### Fine-tuning levels

**Level 1**

Features: Question, correct answer
Label: 0 or 1 (correct or incorrect)

**Level 2**

Features: Question, correct answer, wrong answer
Label: 0 or 1 (conceptual or computational)

**Level 3**

Features: Question, answer (correct or flawed)
Label: 0 or 1 or 2 (correct, conceptual, computational)

**Level 4**

Features: Question, answer (correct or flawed)
Label: 0,1,2,3 (correct, conceptual, computational, skipped step)

**Level 5**

Features: Question, answer (correct or flawed)
Label: Json object with verdict, error type, erroneous_line_number

**Level max**

Features: Question, answer (correct or flawed)
Label: Full json object with verdict, error type, erroneous_line_number, explanation.

---

### **Proposed Pipeline for Conceptual Error Generation**

The process is divided into two stages: a fully automated **Candidate Generation** stage and a manual **Validation & Annotation** stage powered by a specialized GUI.

#### **Stage 1: Automated Candidate Generation**

This stage runs in the background, creating a large pool of potential conceptual errors for human review. For each validated template:

1. **Select Mutation Target:** Programmatically select a line of the `function_code` to modify.
2. **Apply AST Mutation:** Apply a specific, pre-defined logical mutation to the Abstract Syntax Tree (AST) of the `function_code`. Examples of mutations:
    * **Operator Swap:** `ast.Add` ↔ `ast.Sub`, `ast.Mult` ↔ `ast.Div`.
    * **Operand Swap:** For a non-commutative operator like `/` or `-`, swap the left and right operands.
    * **Variable Misuse:** Replace one variable operand with another valid variable from the same scope (e.g., use `num_oranges` instead of `num_apples`).
3. **Generate Flawed Trace:** Execute the mutated AST.
    * If the code fails (e.g., `ZeroDivisionError`), the attempt is logged and discarded.
    * If successful, this produces a `flawed_trace` dictionary where all numerical values are guaranteed to be consistent with the new, flawed logic.
4. **Assemble Candidate Package:** Create a "candidate package" to be sent to the validation GUI. This package contains:
    * The problem `index`.
    * The original, correct `function_code` and `logical_steps`.
    * The mutated, flawed `function_code`.
    * The `flawed_trace`.
    * A description of the mutation (e.g., `{"mutation_type": "operator_swap", "line": "L3", "from": "+", "to": "-"}`).

#### **Stage 2: Manual Validation & Annotation (via GUI)**

This is where the human expert steps in, using an enhanced version of your Streamlit app. The goal is to make the editing task as frictionless as possible.

The GUI for each candidate would present:

* **Reference Pane (Static):**
    1. The full **Problem Text**.
    2. The original, correct **Natural Language Solution**.

* **Task Pane (Dynamic):**
    1. **Logical Change:** A clear, one-line summary of the automated mutation.
        * *Example: "On L3, the operator was changed from `*` to `/`."*
    2. **Value Changes:** A small table showing the key variables on that line and their values before and after the change.
        * *Example: `price` (10) -> 10, `quantity` (5) -> 5, `total_cost` (50) -> **2**.*
    3. **Editable Flawed Solution:** A large text area pre-filled with a naively reconstructed solution.
        * All lines are generated by substituting values from the `flawed_trace` into the original `solution_line_template`s.
        * The line with the logical inconsistency will be nonsensical (e.g., *"To get the total cost, we multiply the price and quantity: <<10 / 5 = 2>>"*). **This is the primary text the user needs to fix.**
    4. **Editable Explanation:** A text input for the `explanation` field of the final JSON label, perhaps pre-filled with a template based on the mutation type.
        * *Example Pre-fill: "The operation on this line is incorrect. It should be multiplication, but division was used."*

* **Action Buttons:**
  * `Accept`: Saves the edited solution and explanation, creating the final SFT-ready data point.
  * `Reject`: Discards the candidate entirely.

**Advantages of this Revised Approach:**

* **Preserves Numerical Integrity:** You are always working from a `flawed_trace` that is mathematically sound, given the logical mutation. The human edits text only.
* **Maximizes Human Efficiency:** The human is not calculating anything. They are performing a constrained editing task: making the text match the numbers. The GUI provides all necessary context to do this quickly.
* **Control:** You have full control over the final quality of every single data point.

---

## **Synopsis: Programmatic Generation of Conceptual Errors**

### **Objective**

Below, we outline a taxonomy of conceptual error types that can be programmatically generated to create a high-quality SFT dataset. The goal is to simulate plausible student mistakes by manipulating the logic of validated "Formalization Templates."

### **Guiding Principle: "Single Point of Failure"**

Our core strategy is to introduce **one single logical error** on a specific line (`N`) of the solution's code representation. All subsequent steps (`N+1`, `N+2`, etc.) are then executed with perfect logic, using the flawed output from line `N` as their input. This isolates the error and simplifies the validation process.

---

### **Error Type 1: Operator Swap**

1. **What it Emulates:** A fundamental misunderstanding of the required mathematical operation.
    * **Examples:** Using `+` instead of `-` to calculate profit (Index `1547`); using `*` instead of `+` to combine totals (Index `1542`); using `*` instead of `/` for unit conversion (Index `1509`).

2. **AST Manipulation Strategy:**
    * Target an `ast.BinOp` node (binary operation).
    * Swap its `op` attribute, e.g., `ast.Mult()` becomes `ast.Div()`, or `ast.Add()` becomes `ast.Sub()`.

3. **Human Validation Task:**
    * The validator sees a reconstructed line where the text implies one operation but the numbers show another.
    * **Example (Index 1547):** The validator might see the text `Each bag makes a profit of 8+4=$12`.
    * **Validator's Edit:** The goal is to make the prose justify the flawed operation. A plausible student might incorrectly believe profit is the sum of costs. The validator edits the text to reflect this flawed reasoning: `"The total money involved per bag is {sale_price}+{cost_price}=${flawed_profit}"`. The new text now matches the flawed calculation.

4. **Challenges & Difficulties:**
    * A simple programmatic string replacement of `+` with `-` in the text is too brittle. The validator must handle the surrounding prose.
    * Must avoid swapping operators for non-numeric types (e.g., string concatenation).

---

### **Error Type 2: Wrong Reference Group**

1. **What it Emulates:** Applying a correct calculation to the wrong set of items.
    * **Examples:** Calculating a percentage of the total population instead of a specific sub-population (Index `1510`: "half the girls" is applied to the whole team); calculating tip on `(price + tax)` instead of just `price` (Index `1500`).

2. **AST Manipulation Strategy:**
    * In an `ast.BinOp` node, identify an `ast.Name` operand that represents a specific group (e.g., `num_girls`).
    * Find another variable in scope representing a different, plausible group (e.g., `total_players`).
    * Swap the `id` of the `ast.Name` node to use the incorrect variable.

3. **Human Validation Task:**
    * The validator sees text that refers to one group but numbers that reflect another.
    * **Example (Index 1510):** A reconstructed line might read `"The team has 10 junior girls because 50 / 2 = 25"`.
    * **Validator's Edit:** The validator adjusts the text to justify the flawed reference. `"Half the team are junior girls, so there are {total_players} / 2 = {flawed_junior_girls} junior girls"`. This is factually incorrect according to the problem, but it is an internally consistent, plausible student error.

4. **Challenges & Difficulties:**
    * Programmatically identifying which variables represent "groups" can be difficult. It will likely rely on heuristics based on variable names.

---

### **Error Type 3: Failure to Update State**

1. **What it Emulates:** A specific "Wrong Reference" error where a student uses a stale initial value instead of a more recent intermediate value in a sequential problem.
    * **Examples:** Using the original weight for a second-stage percentage calculation instead of the remaining weight (Index `1501`); using a starting value for a cumulative increase instead of the previous step's total (Index `1511`).

2. **AST Manipulation Strategy:**
    * This is a targeted application of "Wrong Reference Group."
    * Identify a sequence where `var_C` depends on `var_B`, which depends on `var_A`.
    * In the calculation for `var_C`, replace the operand `var_B` with `var_A`.

3. **Human Validation Task:**
    * The validator sees text implying a sequential update, but numbers reflecting a calculation from the original state.
    * **Example (Index 1501):** The validator sees `"Second Store:45000(.20)=10000"`.
    * **Validator's Edit:** The text is changed to match the flawed logic. `"Second Store: 20% of the original 50000 pounds is removed, so 50000(.20)={flawed_unloaded_amount}"`. This becomes `"{initial_weight}(.20)={flawed_unloaded_amount}"` in the template.

4. **Challenges & Difficulties:**
    * Reliably identifying these state-change chains requires careful dependency analysis of the `function_code`.

---

### **Error Type 4: Operand Swap**

1. **What it Emulates:** Confusion about which number should be the dividend vs. the divisor, or the minuend vs. the subtrahend.
    * **Example (Hypothetical):** For `_672.json`, a student might divide `carrots_per_bag` by `carrots_per_year` instead of the other way around.

2. **AST Manipulation Strategy:**
    * Find an `ast.BinOp` node with `op` as `ast.Div()` or `ast.Sub()`.
    * Swap the `left` and `right` child nodes.

3. **Human Validation Task:**
    * The validator sees a sentence where the text and numbers are completely reversed.
    * **Validator's Edit:** The validator must rewrite the sentence to create a plausible (though incorrect) justification for the swapped logic. For the example above, they might change the text to: `"To find the portion of a bag used per day, we divide the carrots per bag by the total carrots needed: {carrots_per_bag}/{carrots_per_year} = {bags_needed}"`.

4. **Challenges & Difficulties:**
    * This error type places a high editing burden on the human validator, as the entire sentence context usually needs to be rewritten.

---

### **Error Type 5: Input Misrepresentation**

1. **What it Emulates:** Misreading a number from the problem text or using incorrect "world knowledge."
    * **Examples:** Using `17` cans instead of `24` (Index `62`); using `$5` to shovel instead of `$7` (Index `11`).

2. **AST Manipulation Strategy:**
    * Identify an `ast.Assign` node for a variable taken from `question_inputs` or `WK_inputs`.
    * Modify the `value` of its `ast.Constant` node (e.g., perturb `n` to `n+1` or swap with another number from the problem).

3. **Human Validation Task:**
    * **Often requires no edit.** A reconstructed line like `"There are 17 - 10 = 7 cans left"` is already a self-consistent, plausible error.
    * The validator's main job is to confirm that the flawed input is still plausible within the problem's context and accept the change. This is the lowest-effort validation task.

4. **Challenges & Difficulties:**
    * Selecting the flawed value requires care. Random mutation can be nonsensical. A curated list of common WK mistakes (e.g., `dozen=10`, `pi=3`) or swapping with other explicit numbers from the question text is a good strategy.

---

### **Error Type 6: Skipped Step**

1. **What it Emulates:** Completely omitting a necessary calculation, leading to a wrong answer.
    * **Examples:** Forgetting to subtract an expense (Index `16`: the shirt); ignoring a category of items (Index `51`: the bedroom curtains); stopping one step short and reporting an intermediate value as the final answer (Index `724`).

2. **AST Manipulation Strategy (Complex):**
    1. **Deletion:** Delete an `ast.Assign` node (e.g., the line calculating `bedroom_curtain_area`).
    2. **Rewiring:** Find the subsequent `ast.Assign` node that uses the now-deleted variable. Modify its expression to remove that variable (e.g., `total - living_room_area - bedroom_curtain_area` becomes `total - living_room_area`).

3. **Human Validation Task:**
    * The validator sees an abridged solution with a logical leap.
    * **Example (Index 51):** The final line would be reconstructed as `"Finally, subtract the square footage of the living room curtains from the total: 192 - 24 = 168 square feet"`.
    * **Validator's Edit:** The validator confirms this abridged text is plausible. They might simplify it to `"The remaining fabric is 192 - 24 = 168 square feet"`. They would also need to remove the corresponding original line from the full solution text block in the GUI.

4. **Challenges & Difficulties:**
    * The "rewiring" step is the most technically difficult part of this entire plan and is prone to causing `NameError` if not handled perfectly.
    * The "Omitted Final Step" sub-type is much easier: simply change the `return` statement to an intermediate variable. This should be implemented first.

---

### **Error Type 7: Unit Handling / Conversion Error**

1. **What it Emulates:** A failure to correctly manage units. This is a "meta-category" that uses our other generators.
    * **Examples:** Using the wrong operator for a conversion (`*` instead of `/`) is an **Operator Swap**. Forgetting a conversion factor (`dozen` = 12) is a **Skipped Step**. Adding incompatible units (months + years) is **Incorrect Variable Usage**.

2. **AST Manipulation Strategy:**
    * We don't need a new manipulation type. Instead, we programmatically **identify unit conversion steps** and apply one of our existing generators (`Operator Swap`, `Skipped Step`, etc.) to that specific step.
    * We can identify these steps by looking for known conversion constants (`12`, `60`) or variable names containing unit words (`inches`, `feet`).

3. **Human Validation Task:**
    * The task is identical to that of the underlying error type being used.
    * **Example (Index 1531, Incorrect Variable Usage):** A student adds months to years. The validator sees `So in total it all took 2+4+48+2=56 years`.
    * **Validator's Edit:** They might simplify the text to remove unit confusion, making the flawed summation plausible: `"The total time is 2+4+48+2 = {flawed_total_years}"`.

4. **Challenges & Difficulties:**
    * The main challenge is the heuristic-based identification of "unit conversion" steps. A misclassification is not critical, as it will still produce a valid conceptual error, just perhaps not a "unit" one.


### **Error Type 8: Incorrect Final Answer Selection**

1. **What it Emulates:** A student performs all intermediate calculations correctly but fails to answer the specific question asked in the final step. They might report a valid intermediate value (e.g., total items instead of remaining items) or misinterpret which calculated variable represents the requested answer. This is distinct from a `Skipped_Step` where a necessary calculation is omitted entirely. Here, the calculation for the correct answer is often present, but simply not returned.

2. **AST Manipulation Strategy:**
    * This error type does not typically involve modifying an intermediate calculation. Instead, it targets the final `return` statement of the `function_code`.
    * Identify an intermediate variable in the `correct_trace` that is a plausible but incorrect final answer.
    * In the `function_code`'s AST, change the `value` of the `ast.Return` node from the correct final variable to the identified intermediate variable (e.g., `return final_answer` becomes `return number_of_new_hires`).

3. **Human Validation Task:**
    * The validator is presented with a solution where the reasoning and calculations are perfectly sound up to the final line. The final sentence or `####` value is simply incorrect.
    * **Example (Index 1132):** The validator sees the correct calculation for new hires (`213`) but the final answer is reported as `213` instead of `852 + 213 = 1065`.
    * **Validator's Edit:** The validator simply needs to adjust the final sentence to match the flawed output. For example, changing `"Therefore, there are now 1065 employees"` to `"Therefore, 213 new employees were hired"`. This is a low-effort task focused on the concluding statement.

4. **Challenges & Difficulties:**
    * The primary challenge is programmatically identifying which intermediate variables are "plausible" incorrect answers. This may require heuristics (e.g., variables calculated in the penultimate step) or manual tagging within the `logical_steps` of the Formalization Template.


### **Error Type 9: Incorrect Formula Application**

1. **What it Emulates:** A student correctly identifies the necessary numerical inputs but combines them using a structurally incorrect formula. This goes beyond a simple operator swap; the entire equation or logical construct is wrong for the task.
    * **Examples:** Using a simple average (`(a+b)/2`) when a weighted average is required; fundamentally misusing how ratios apply to a total; applying a dimensional property (like 'dots per inch') to the wrong kind of quantity (like 'area' instead of 'length').

2. **AST Manipulation Strategy:**
    * This is a complex category to generate programmatically. It would involve replacing an entire expression with another structurally different one.
    * For example, an `ast.BinOp` node for a weighted average `(w1*a + w2*b) / (w1+w2)` might be replaced with a simple average `(a+b)/2`. This requires identifying common formulaic mistakes and having pre-defined AST templates for both the correct and incorrect formulas.

3. **Human Validation Task:**
    * The validator sees a calculation that is nonsensical for the problem type.
    * **Example (Index 1265):** The validator might see `"The average monthly bill is ($30 + $24) / 2 = $27"`.
    * **Validator's Edit:** The validator adjusts the text to justify this flawed approach. `"To find the average, we take the average of the two monthly rates: ($30 + $24) / 2 = $27"`. This text now matches the flawed formula.

4. **Challenges & Difficulties:**
    * Programmatically identifying which lines of code correspond to which high-level formulas is a significant challenge. It would likely require semantic analysis or special tagging in the Formalization Template.

---

I have analyzed the 100 samples from the provided CSV file. The existing taxonomy covers the majority of cases well, but the analysis reveals two recurring error patterns that are not precisely captured by the current definitions.

To accurately classify all samples, I propose adding the following two error types to your taxonomy.

---

### **Error Type 10: Misinterpreted Scoping / Precedence**

1. **What it Emulates:** A misunderstanding of how a natural language phrase maps to mathematical order of operations or grouping. This is common with phrases like "X less than Y times Z," where a student might incorrectly calculate `Y * (Z - X)` instead of `(Y * Z) - X`. It is not a simple operator swap, but an error in the structure of the expression itself.
2. **AST Manipulation Strategy:**
    * This involves restructuring an `ast.BinOp` node. For example, `(Y * Z) - X` which is `ast.BinOp(left=ast.BinOp(left=Y, op=ast.Mult, right=Z), op=ast.Sub, right=X)` might be incorrectly transformed into `ast.BinOp(left=Y, op=ast.Mult, right=ast.BinOp(left=Z, op=ast.Sub, right=X))`.
    * This manipulates the tree structure to change which operations are performed first, directly modeling the precedence error.
3. **Human Validation Task:**
    * The validator sees a calculation that is mathematically valid but based on a flawed parsing of the problem statement.
    * **Example (Index 1337):** The validator sees the text `2(x-5)=13` derived from "5 less than twice as many pairs".
    * **Validator's Edit:** The user would adjust the prose to justify this flawed grouping, perhaps by rewriting the logic to something like: "First, find the difference between the number of shoes Becky owns and 5, then double it: `2(x-5)=13`."
4. **Challenges & Difficulties:**
    * Identifying these phrases programmatically requires robust NLP parsing or pattern matching.
    * Generating plausible alternative text during the human validation step can be challenging, as it requires inventing a justification for the flawed grouping.

---

### **Error Type 11: Extraneous Operation / Invented Method**

1. **What it Emulates:** The student, failing to identify the correct solution path, invents a completely unsupported mathematical procedure. This goes beyond using a wrong operator or variable; it involves introducing a calculation that has no basis in the problem's text.
2. **AST Manipulation Strategy:**
    * This is a significant mutation. It involves replacing a correct `ast.Assign` node's value with a new, structurally different expression.
    * For example, replacing `ast.Call(func=ast.Name(id='sqrt'), ...)` with an `ast.BinOp` that averages two unrelated variables.
3. **Human Validation Task:**
    * The validator is presented with a solution line that uses a nonsensical method to arrive at a value.
    * **Example (Index 1323):** The validator sees text like `"To turn it into a square, the side length would be (6 + 24) / 2 = 15 feet."`
    * **Validator's Edit:** The validator must make the prose match this invented logic. The existing text is already a plausible (though incorrect) student justification, so the task is often just to approve the generated sample.
4. **Challenges & Difficulties:**
    * Generating *plausible* but incorrect methods is the primary challenge. Randomly inserting operations will likely produce nonsense. This will require a curated set of common but incorrect heuristics (e.g., "when in doubt, average them").

### **Error Type 12: Algebraic Simplification Error**

1. **What it Emulates:** A student correctly sets up an algebraic equation but makes a mistake during a simplification step. This is a procedural error in applying the rules of algebra.
    * **Examples:** Incorrectly combining like terms (e.g., `3x + x = 2x`); incorrectly distributing a value or a negative sign across parentheses.
2. **AST Manipulation Strategy:**
    * This is a targeted transformation that mimics a specific algebraic rule violation.
    * For `3x + x = 4x`, the `ast.BinOp` representing `3x+x` would be replaced by an `ast.BinOp` that results in `2x`. This is not a random change but a simulation of a common cognitive error. It requires modifying the coefficients in the expression's AST representation post-setup but pre-solving.
3. **Human Validation Task:**
    * The validator sees a line of algebraic reasoning that is internally inconsistent.
    * **Example (Index 1420):** The validator would see `Combining like terms, we get 2w - 6 = 54` following the setup `3w - 6 + w = 54`.
    * **Validator's Edit:** The text is often already plausible, as it describes the *intended* operation, even if executed incorrectly. The validator's role is to confirm that this is a common student mistake and accept the sample.
4. **Challenges & Difficulties:**
    * Generating these requires identifying expressions with like terms or other algebraic constructs ripe for simplification errors. The mutations must be specific (e.g., change the coefficient after combination) rather than random.

### **Error Type 13: Constraint Violation**

1. **What it Emulates:** A student understands the individual numbers and basic operations but fails to satisfy a key qualitative condition or constraint of the problem. This is not an arithmetic or algebraic mistake, but a failure in the logical setup.
    * **Examples:** Calculating costs that exceed a stated budget; providing fewer items than required for a group (Index `803`); failing to select the "least" or "most" of a set of options when required.
2. **AST Manipulation Strategy:** This is a high-level logical error that is difficult to generate via simple AST mutations. It would likely involve identifying a constraint in the problem's logic (e.g., `num_bags >= num_students`) and then generating a solution that violates it, perhaps by using `floor()` division where `ceil()` is needed, or by selecting a non-optimal value from a list of calculated options.
3. **Human Validation Task:** The validator is presented with a solution that is numerically self-consistent but fails to solve the actual problem posed. For instance, the math for buying 10 bags for 11 students might be correct, but the solution is invalid because it leaves one student without a bag. The validator must confirm that the core constraint has been violated.
4. **Challenges & Difficulties:** Programmatically identifying and then violating these high-level logical constraints is the primary challenge. This type of error generation would likely rely on more advanced analysis of the problem's semantic structure rather than just the `function_code`.

---

### Running the conceptual error validation app

Run this in the terminal from the project root:

```bash
streamlit run validate_candidates.py --theme.base "light" -- --candidates-dir data/conceptual-error-candidates
```

It will open the validation app in the browser. The erroneous line number will tell you which line the error was injected; you can ignore all previous lines.

Some pointers:

1. Most of the time, at most a mild text edit will be needed in the erroneous line, and no change will be needed for subsequent lines. Note that, typically, values will not have to be changed (in particular, you need not verify any of the computations, that is all handled programmatically). The main thing to watch out for is when numbers appear in word-form in the text, and for operators that should have been changed but did not get changed.
2. If you find that many changes are needed, or that it's getting to be a pain, simply skip and move onto the next problem until you find one that's sufficiently simple.
3. If you find the induced change is absurd or unrealistic, then simply reject the sample.
4. Note: there are TONS of samples, so for a first pass it should be totally fine to simply skip over samples that appear too complicated. In all likelihood, we might already get enough samples with minor/no modification needed at all!