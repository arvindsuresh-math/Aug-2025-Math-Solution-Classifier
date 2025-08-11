def solve():
    """Index: 1878.
    Returns: Emma's age when her sister is 56.
    """
    # L1
    emma_current_age = 7 # Emma is 7 years old
    sister_age_difference = 9 # her sister is 9 years older than her
    sister_current_age = emma_current_age + sister_age_difference

    # L2
    sister_future_age = 56 # when her sister is 56
    years_to_future = sister_future_age - sister_current_age

    # L3
    emma_future_age = emma_current_age + years_to_future

    # FA
    answer = emma_future_age
    return answer