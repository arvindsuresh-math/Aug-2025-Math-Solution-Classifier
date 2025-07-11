def solve():
    """Index: 534.
    Returns: Jessica's current age.
    """
    # L1
    claire_age_in_two_years = 20 # Claire will be 20 years old
    years_from_now = 2 # In two years
    claire_current_age = claire_age_in_two_years - years_from_now

    # L2
    jessica_age_difference = 6 # Jessica is six years older than Claire
    jessica_current_age = claire_current_age + jessica_age_difference

    # FA
    answer = jessica_current_age
    return answer