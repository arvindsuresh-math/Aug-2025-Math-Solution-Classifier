def solve():
    """Index: 3499.
    Returns: Antonio's age in months.
    """
    # L1
    target_age_years = 10 # she will be 10 years old
    months_per_year = 12 # WK
    isabella_target_age_months = target_age_years * months_per_year

    # L2
    months_until_target_age = 18 # In 18 months
    isabella_current_age_months = isabella_target_age_months - months_until_target_age

    # L3
    isabella_age_multiple = 2 # twice as old as Antonio
    antonio_current_age_months = isabella_current_age_months / isabella_age_multiple

    # FA
    answer = antonio_current_age_months
    return answer