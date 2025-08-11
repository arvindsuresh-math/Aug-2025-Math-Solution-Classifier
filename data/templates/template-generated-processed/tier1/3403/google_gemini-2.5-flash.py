def solve():
    """Index: 3403.
    Returns: the sum of their ages in 5 years.
    """
    # L1
    will_age_past = 4 # 4 years old 3 years ago
    years_ago = 3 # 3 years ago
    will_age_now = will_age_past + years_ago

    # L2
    diane_age_multiplier = 2 # twice as old
    diane_age_now = diane_age_multiplier * will_age_now

    # L3
    years_future = 5 # in 5 years
    will_age_future = will_age_now + years_future

    # L4
    diane_age_future = diane_age_now + years_future

    # L5
    sum_ages_future = will_age_future + diane_age_future

    # FA
    answer = sum_ages_future
    return answer