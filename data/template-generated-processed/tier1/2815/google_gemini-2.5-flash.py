def solve():
    """Index: 2815.
    Returns: Terry's current age.
    """
    # L1
    multiplier = 4 # 4 times the age
    nora_current_age = 10 # Nora is currently 10 years old
    years_from_now = 10 # In 10 years
    terry_age_in_future = multiplier * nora_current_age

    # L2
    terry_current_age = terry_age_in_future - years_from_now

    # FA
    answer = terry_current_age
    return answer