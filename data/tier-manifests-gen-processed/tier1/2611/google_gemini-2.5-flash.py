def solve():
    """Index: 2611.
    Returns: Trevor's age when his older brother is three times as old as Trevor is now.
    """
    # L1
    trevor_current_age = 11 # Trevor is currently 11 years old
    multiplier = 3 # three times as old
    brother_target_age = trevor_current_age * multiplier

    # L2
    brother_current_age = 20 # his older brother is 20 years old
    age_difference = brother_current_age - trevor_current_age

    # L3
    trevor_future_age = brother_target_age - age_difference

    # FA
    answer = trevor_future_age
    return answer