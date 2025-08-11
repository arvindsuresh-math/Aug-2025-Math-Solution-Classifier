# Data description

## Data sources

These come in two forms:

1. **Manual**: This consists of ~1900 hand-crafted samples consisting of problems from the GSM8K train-set, along with flawed answers containing conceptual or computational errors. A complete catalog of manually generated errors is found here:

    ./data/manually_generated_errors_final.csv

2. **Programmatic**: These samples are created as follows. First, `gemini-2.5-flash` is prompted to generate "formalization templates" for each problem. Then, the templates are used to inject errors into the solutions:
    i. The computational errors are high-quality enough that they do not require review/validation by a human.
    The catalog for these errors is found here:

        ./data/computational-errors-generated/computational_error_catalog.csv

    ii. The conceptual errors are more subtle, requiring changes to the text that are not easily implemented programmatically, so these are left to humans to review and validate. The catalog for a shortlist of ~1300 (unvalidated) errors can be found here:

        ./conceptual-error-candidates/conceptual_candidates_shortlist.csv

    Each `person` in `["ali", "arvind", "ling", "mauro", "yewei"]` is assigned ~350 samples to validate from the shortlist. The validation is done via the help of the streamlit app found here:

        ./validate_candidates.py

    Every time the `person` accepts a sample (possibly with edits) via the app, the corresponding sample is saved as a json file inside the parent directory `./data/conceptual-errors-accepted`. Each `person` has their own individual validation catalog that tracks the metadata of their validation process, found here:

        ./data/conceptual-error-candidates/validation_catalog_{person}.csv