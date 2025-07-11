def solve():
    """Index: 1065.
    Returns: how much more pounds John gets out of wraps versus sleeves.
    """
    # L1
    raw_squat_weight = 600 # raw squat of 600 pounds
    wraps_percentage_increase = 0.25 # Wraps add 25%
    wraps_added_weight = raw_squat_weight * wraps_percentage_increase

    # L2
    sleeves_added_weight = 30 # Sleeves add 30 pounds
    difference_wraps_sleeves = wraps_added_weight - sleeves_added_weight

    # FA
    answer = difference_wraps_sleeves
    return answer