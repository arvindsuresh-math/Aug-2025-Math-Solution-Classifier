def solve():
    """Index: 534.
    Returns: Jessica's current age.
    """
    # L1
    claire_age_in_2_years = 20 # Claire will be 20 years old
    years_until_20 = 2 # In two years
    claire_current_age = claire_age_in_2_years - years_until_20

    # L2
    jessica_older_by = 6 # Jessica is six years older than Claire
    jessica_current_age = claire_current_age + jessica_older_by

    # FA
    answer = jessica_current_age
    return answer