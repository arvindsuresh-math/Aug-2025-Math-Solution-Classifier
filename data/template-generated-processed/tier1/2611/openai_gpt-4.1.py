def solve():
    """Index: 2611.
    Returns: Trevor's age when his older brother is three times as old as Trevor is now.
    """
    # L1
    trevor_age_now = 11 # Trevor is currently 11 years old
    multiplier = 3 # three times as old as Trevor is now
    brother_target_age = trevor_age_now * multiplier

    # L2
    brother_age_now = 20 # his older brother is 20 years old
    age_difference = brother_age_now - trevor_age_now

    # L3
    trevor_age_when_brother_target = brother_target_age - age_difference

    # FA
    answer = trevor_age_when_brother_target
    return answer