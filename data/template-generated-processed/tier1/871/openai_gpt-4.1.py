def solve():
    """Index: 871.
    Returns: the year Julia was born in.
    """
    # L1
    wayne_age = 37 # Wayne is 37 years old
    peter_older = 3 # Peter is 3 years older than him
    peter_age = wayne_age + peter_older

    # L2
    julia_older = 2 # Julia is 2 years older than Peter
    julia_age = julia_older + peter_age

    # L3
    current_year = 2021 # In 2021
    julia_birth_year = current_year - julia_age

    # FA
    answer = julia_birth_year
    return answer