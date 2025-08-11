def solve():
    """Index: 5685.
    Returns: Cornelia's current age.
    """
    # L1
    kilee_current_age = 20 # Kilee is currently 20 years old
    years_in_future = 10 # In 10 years
    kilee_age_in_future = kilee_current_age + years_in_future

    # L2
    age_multiplier = 3 # three times as old
    cornelia_age_in_future = age_multiplier * kilee_age_in_future

    # L3
    cornelia_current_age = cornelia_age_in_future - years_in_future

    # FA
    answer = cornelia_current_age
    return answer