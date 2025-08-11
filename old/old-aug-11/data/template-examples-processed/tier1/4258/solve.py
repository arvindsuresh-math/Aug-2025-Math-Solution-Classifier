def solve():
    """Index: 4258.
    Returns: the number of horses Mickey mounts per week.
    """
    # L1
    days_in_week = 7 # WK
    minnie_more_than_week = 3 # three more horses per day than there are days in a week
    minnie_per_day = days_in_week + minnie_more_than_week

    # L2
    multiplier_for_twice = 2 # twice as many horses
    twice_minnie = minnie_per_day * multiplier_for_twice

    # L3
    mickey_less_than_twice_minnie = 6 # six less than twice as many horses
    mickey_per_day = twice_minnie - mickey_less_than_twice_minnie

    # L4
    mickey_per_week = mickey_per_day * days_in_week

    # FA
    answer = mickey_per_week
    return answer