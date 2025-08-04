# Experiments for academic-oriented project

There are two broad categories:

1. **Discriminative**: The model is treated as a "feature extractor". That is, the labels (correct, flawed, etc.) are encoded as digits (0, 1 etc.), and a custom classifier head is attached to the model. This classifier head accepts the vector representation of the last token in the model's response, and maps this to a probability distribution over the classes. Although this classifier head could be any traditional ML soft classifier, for simplicity we use only a linear (i.e. softmax regression) classifier. Thus, during fine-tuning, when the model weights as well as the classifier head's weights are updated, the model learns to extract features to look like vectors living in linearly separable clusters. Note that the loss function for this type of fine-tuning is cross-entropy using the numerically encoded classes (**not** the token-space).

2. **Generative**: The model is treated as an auto-completer (i.e. chat assistant) and asked to respond to the prompt in a structured format (typically a JSON object). This version is simpler in that there is no need for a custom classifier head to be attached, but on the other hand, it is also more sophisticated because the loss function used is the usual "cross-entropy for the next token" loss function on the token-space. Since the models we are testing out (`microsoft/Phi-4-mini-instruct`, `Qwen/Qwen3-4B`) are already very capable at mathematical reasoning, the main aims of the fine-tuning are to (a) refine the model's understanding of the distinction between conceptual and computational errors (as we are defining them), and (b) ensure the model learns to structure its output in the desired format.

## 1. Discriminative experiments

**Total experiments**: 4 (2 classification types × 2 models)

### 1.1 Experimental factors

Each discriminative experiment is defined by the following choices:

1. **Classification type**: "binary" or "ternary"
2. **Model**: "Qwen/Qwen3-4B" or "microsoft/Phi-4-mini-instruct"

### 1.2 Binary classification

#### 1.2.1 Sample description

- **Input**: Consists of a problem along with a solution (correct or flawed), and a minimal prompt directing the model to determine whether the solution is correct or flawed.
- **Labels**: 0 (correct) and 1 (flawed)

#### 1.2.2 Dataset description

Let $A$ denote the subset of GSM8K problems for which there exists a sample with conceptual error (either manually generated, or programmatically generated and then validated by a human), and let $N = |A|$. Then, we choose a subset $B$ of GSM8K problems with these properties:

1. $B$ is disjoint from $A$.
2. $|B| = |A| = N$.
3. For each problem in $B$, there exists a computational-error sample (priority will be given to samples made manually).

Then, the dataset will contain a total of $4N$ samples, with $2N$ distinct problems, chosen as follows:

1. $N$ conceptual error samples for problems in $A$.
2. $N$ computational error samples for problems in $B$.
3. $N$ correct samples for problems in $A$.
4. $N$ correct samples for problems in $B$.

In this way, the dataset will be perfectly balanced between the two classes 0 and 1.

### 1.3 Ternary classification

#### 1.3.1 Sample description

- **Input**: Consists of a problem along with a solution (correct or flawed), and a minimal prompt directing the model to determine whether the solution is correct, or has a computational error, or has a conceptual error.
- **Labels**: 0 (correct), 1 (conceptual error), and 2 (computational error)

#### 1.3.2 Dataset description

Let $A$ denote the subset of GSM8K problems for which there exists a sample with conceptual error (either manually generated, or programmatically generated and then validated by a human), and let $N = |A|$.

Then, the dataset will contain a total of $3N$ samples, with $3$ versions of each of the $N$ problems in $A$:

1. $N$ conceptual error samples.
2. $N$ original, correct samples (drawn from GSM8K).
3. $N$ computational error samples (priority is given first to any manually-generated samples, and then, to the programmatically-generated samples).

Note: A small portion of the problems in $A$ may not have an associated computational-error sample, in which case they will be pruned out.

In this way, the dataset will be perfectly balanced between the classes 0, 1, and 2.

## 2. Generative experiments

**Total experiments**: 64 (2 classification types × 2 dataset strategies × 2 explanation choices × 2 ELN choices × 2 formatting choices × 2 models)

### 2.1 Experimental factors

Each generative experiment is defined by the following choices:

1. **Classification type**: "binary" or "ternary"
2. **Dataset assembly strategy**: "4N" or "3N"
3. **Explanation field**: "include" or "exclude"
4. **Erroneous line number**: "include" or "exclude"
5. **Solution formatting**: "nl" (natural language) or "dict" (line-numbered dictionary)
6. **Model**: "Qwen/Qwen3-4B" or "microsoft/Phi-4-mini-instruct"

### 2.2 Dataset assembly strategies

#### 2.2.1 4N strategy
Uses the same dataset construction as discriminative binary classification (section 1.2.2): $4N$ samples across $2N$ distinct problems from sets $A$ and $B$.

#### 2.2.2 3N strategy
Uses the same dataset construction as discriminative ternary classification (section 1.3.2): $3N$ samples across $N$ distinct problems from set $A$ only.

### 2.3 Input formatting

#### 2.3.1 Natural language (nl)
The solution is presented as continuous text, exactly as it appears in the original GSM8K dataset or generated error samples.

#### 2.3.2 Dictionary (dict)
The solution is formatted as a dictionary mapping line identifiers to solution lines:
```json
{
    "L1": "First line of solution",
    "L2": "Second line of solution", 
    "FA": "Final answer line"
}
```

### 2.4 Output specifications

#### 2.4.1 Binary classification outputs

**Verdict only:**
```json
{
    "verdict": "correct" | "flawed"
}
```

**Verdict + erroneous line number (dict format):**
```json
{
    "verdict": "correct" | "flawed",
    "erroneous_line_number": "L1" | "L2" | "FA" | null
}
```

**Verdict + erroneous line number (nl format):**
```json
{
    "verdict": "correct" | "flawed", 
    "erroneous_line": "Full text of the erroneous line" | null
}
```

**Verdict + explanation:**
```json
{
    "verdict": "correct" | "flawed",
    "explanation": "Brief explanation of the error" | null
}
```

**All fields combined (dict format):**
```json
{
    "verdict": "correct" | "flawed",
    "erroneous_line_number": "L1" | "L2" | "FA" | null,
    "explanation": "Brief explanation of the error" | null
}
```

**All fields combined (nl format):**
```json
{
    "verdict": "correct" | "flawed",
    "erroneous_line": "Full text of the erroneous line" | null,
    "explanation": "Brief explanation of the error" | null
}
```

#### 2.4.2 Ternary classification outputs

**Verdict only:**
```json
{
    "verdict": "correct" | "conceptual_error" | "computational_error"
}
```

**Verdict + erroneous line number (dict format):**
```json
{
    "verdict": "correct" | "conceptual_error" | "computational_error",
    "erroneous_line_number": "L1" | "L2" | "FA" | null
}
```

**Verdict + erroneous line number (nl format):**
```json
{
    "verdict": "correct" | "conceptual_error" | "computational_error",
    "erroneous_line": "Full text of the erroneous line" | null
}
```

**Verdict + explanation:**
```json
{
    "verdict": "correct" | "conceptual_error" | "computational_error",
    "explanation": "Brief explanation of the error" | null
}
```

**All fields combined (dict format):**
```json
{
    "verdict": "correct" | "conceptual_error" | "computational_error",
    "erroneous_line_number": "L1" | "L2" | "FA" | null,
    "explanation": "Brief explanation of the error" | null
}
```

**All fields combined (nl format):**
```json
{
    "verdict": "correct" | "conceptual_error" | "computational_error",
    "erroneous_line": "Full text of the erroneous line" | null,
    "explanation": "Brief explanation of the error" | null
}
```

### 2.5 Field specifications

- **verdict**: Always required. For binary: "correct" or "flawed". For ternary: "correct", "conceptual_error", or "computational_error".
- **erroneous_line_number**: Line identifier (e.g., "L1", "FA") when verdict indicates an error, `null` when verdict is "correct". Only used with dict formatting.
- **erroneous_line**: Full text of the erroneous line when verdict indicates an error, `null` when verdict is "correct". Only used with nl formatting.
- **explanation**: Brief explanation of the error when verdict indicates an error, `null` when verdict is "correct".

### 2.6 Experiment naming convention

```
gen_{binary|ternary}_{4N|3N}_{explain|no_explain}_{eln|no_eln}_{dict|nl}_{qwen|phi4}
```

Examples:
- `gen_binary_4N_explain_eln_dict_qwen`
- `gen_ternary_3N_no_explain_no_eln_nl_phi4`

## 3. Summary

### 3.1 Discriminative experiments (4 total)
- `disc_binary_qwen`
- `disc_binary_phi4`
- `disc_ternary_qwen`
- `disc_ternary_phi4`

### 3.2 Generative experiments (64 total)
All combinations of:
- Classification: binary, ternary
- Dataset: 4N, 3N
- Explanation: explain, no_explain
- ELN: eln, no_eln
- Format: dict, nl
- Model: qwen, phi4

### 3.3 Total experiments
**68 experiments** (4 discriminative + 64 generative)

### 3.4 Resource requirements
- Estimated time per experiment: 10-15 minutes
- Total compute time: ~11-17 hours across 5 researchers
- Average per researcher: ~13-14 experiments (~2.5-3.5 hours)


### sft experiment assignments

4 experiments per person (or how much ever is possible)

1. Ali: 
- Classification: ternary
- Dataset: 4N, 3N
- Explanation: no_explain
- ELN: no_eln
- Format: nl
- Model: qwen, phi4

Done: 3N (left: 4N)

2. Mauro:
- Classification: binary
- Dataset: 4N, 3N
- Explanation: no_explain
- ELN: no_eln
- Format: nl
- Model: qwen, phi4

Done: 3N (left: 4N)

3. Yewei:
- Classification: ternary
- Dataset: 4N, 3N
- Explanation: no_explain
- ELN: no_eln
- Format: nl
- Model: qwen, phi4

4. Ling:
- Classification: binary
- Dataset: 4N, 3N
- Explanation: no_explain
- ELN: no_eln
- Format: nl
- Model: qwen, phi4

5. Arvind: 
- Classification: ternary
- Dataset: 4N, 3N
- Explanation: explain
- ELN: eln
- Format: nl
- Model: qwen, phi4

Done: all with phi4 (not touched qwen3)