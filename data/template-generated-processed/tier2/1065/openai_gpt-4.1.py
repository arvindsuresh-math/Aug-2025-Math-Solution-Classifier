def solve():
    """Index: 1065.
    Returns: how many more pounds wraps add to John's squat compared to sleeves.
    """
    # L1
    raw_squat = 600 # raw squat of 600 pounds
    wraps_percent = 0.25 # Wraps add 25% to his squat
    wraps_added = raw_squat * wraps_percent

    # L2
    sleeves_added = 30 # Sleeves add 30 pounds
    more_pounds_wraps_than_sleeves = wraps_added - sleeves_added

    # FA
    answer = more_pounds_wraps_than_sleeves
    return answer