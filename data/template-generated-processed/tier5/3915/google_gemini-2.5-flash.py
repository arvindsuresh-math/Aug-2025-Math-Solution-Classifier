def solve():
    """Index: 3915.
    Returns: the number of shots Jordan blocked in the fourth period.
    """
    # L2
    shots_blocked_first_period = 4 # blocked four shots
    multiplier_second_period = 2 # twice as many shots
    shots_blocked_second_period = multiplier_second_period * shots_blocked_first_period

    # L3
    fewer_than_second_period = 3 # three fewer than in the second period
    shots_blocked_third_period = shots_blocked_second_period - fewer_than_second_period

    # L4
    total_shots_blocked = 21 # blocked 21 shots in all
    sum_known_periods = shots_blocked_first_period + shots_blocked_second_period + shots_blocked_third_period

    # L5
    shots_blocked_fourth_period = total_shots_blocked - sum_known_periods

    # FA
    answer = shots_blocked_fourth_period
    return answer