import json
import pandas as pd

# Read the JSONL file
data = []
with open('final-test-set.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line.strip()))

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('final-test-set.csv', index=False)
print('Conversion complete: final-test-set.csv created')