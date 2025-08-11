def solve():
    """Index: 2815.
    Returns: Terry's current age.
    """
    # L1
    nora_current_age = 10 # Nora is currently 10 years old
    terry_future_multiplier = 4 # 4 times the age that Nora is currently
    terry_in_10_years = terry_future_multiplier * nora_current_age

    # L2
    years_until_future = 10 # In 10 years
    terry_current_age = terry_in_10_years - years_until_future

    # FA
    answer = terry_current_age
    return answer