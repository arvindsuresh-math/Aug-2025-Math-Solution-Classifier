def solve():
    """Index: 6130.
    Returns: Heracles' current age.
    """
    # L1
    audrey_older_than_heracles = 7 # Audrey is 7 years older than Heracles
    years_in_future = 3 # In 3 years
    audrey_age_in_3_years_relative_to_heracles_now = audrey_older_than_heracles + years_in_future

    # L2
    # The problem states "In 3 years, Audrey will be twice as old as Heracles is now."
    # This means Audrey's age in 3 years = 2 * Heracles' current age.
    # From L1, Audrey's age in 3 years = Heracles' current age + audrey_age_in_3_years_relative_to_heracles_now.
    # So, Heracles' current age + audrey_age_in_3_years_relative_to_heracles_now = 2 * Heracles' current age.
    # This simplifies to Heracles' current age = audrey_age_in_3_years_relative_to_heracles_now.
    # The calculation in L2 (10 * 2 = 20) is calculating Audrey's age in 3 years, assuming Heracles' current age is 10.
    double_multiplier = 2 # twice as old
    audrey_age_in_3_years = audrey_age_in_3_years_relative_to_heracles_now * double_multiplier

    # L3
    # As derived from the problem statement and L1/L2, Heracles' current age is equal to audrey_age_in_3_years_relative_to_heracles_now.
    heracles_age_now = audrey_age_in_3_years_relative_to_heracles_now

    # FA
    answer = heracles_age_now
    return answer