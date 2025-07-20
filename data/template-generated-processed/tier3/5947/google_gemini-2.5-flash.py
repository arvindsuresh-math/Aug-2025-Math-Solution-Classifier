def solve():
    """Index: 5947.
    Returns: the birth year of Karina's brother.
    """
    # L1
    karina_current_age = 40 # her current age is 40
    age_ratio = 2 # twice as old as her brother
    brother_current_age = karina_current_age / age_ratio

    # L2
    karina_birth_year = 1970 # Karina was born in 1970
    brother_birth_year = karina_birth_year + brother_current_age

    # FA
    answer = brother_birth_year
    return answer