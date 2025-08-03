# Base Datasets for SFT Experiments

Created on: 2025-07-31 09:41:52
Random seed: 42

## Dataset Files

### base_3N_dataset_sanitized.csv
- **Strategy**: Ternary classification (3N)
- **Samples**: 5,319 total (1,773 unique problems × 3 samples each)
- **Structure**: Each problem has exactly 3 samples: correct, conceptual_error, computational_error
- **Use case**: Ternary classification experiments (correct vs conceptual_error vs computational_error)

### base_4N_dataset_sanitized.csv
- **Strategy**: Binary classification (4N)
- **Samples**: 7,524 total (3,762 unique problems × 2 samples each)
- **Structure**: 
  - Set A (1,881 problems): correct + conceptual_error
  - Set B (1,881 problems): correct + computational_error
- **Use case**: Binary classification experiments (correct vs flawed)

## Column Descriptions

- `index`: GSM8K problem index
- `tier`: Problem difficulty tier (tier1-tier4)
- `question`: Problem statement
- `correct_answer`: Correct solution from GSM8K
- `wrong_answer`: Solution text (correct for 'correct' samples, flawed for error samples)
- `error_type`: 'correct', 'conceptual_error', or 'computational_error'
- `erroneous_line_number`: Line number where error occurs (null for correct samples)
- `explanation`: Error explanation (null for correct samples)
- `error_subtype`: Specific error subtype (null for correct samples)
- `source`: 'gsm8k' (correct samples), 'manual', or 'programmatic'
- `solution_length`: Number of solution lines
- `relative_line_position`: Position of error relative to solution length

## Usage in Colab

```python
import pandas as pd

# Load datasets
df_3N = pd.read_csv('base_3N_dataset_sanitized.csv')
df_4N = pd.read_csv('base_4N_dataset_sanitized.csv')

# Verify structure
print("3N dataset composition:")
print(df_3N['error_type'].value_counts())

print("4N dataset composition:")  
print(df_4N['error_type'].value_counts())
```
