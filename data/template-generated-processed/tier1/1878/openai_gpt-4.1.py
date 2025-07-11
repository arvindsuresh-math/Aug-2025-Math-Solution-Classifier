def solve():
    """Index: 1878.
    Returns: Emma's age when her sister is 56 years old.
    """
    # L1
    emma_age = 7 # Emma is 7 years old
    sister_older_by = 9 # her sister is 9 years older than her
    sister_age = emma_age + sister_older_by

    # L2
    sister_target_age = 56 # her sister is 56
    years_until_sister_56 = sister_target_age - sister_age

    # L3
    emma_age_when_sister_56 = emma_age + years_until_sister_56

    # FA
    answer = emma_age_when_sister_56
    return answer