def solve():
    """Index: 1927.
    Returns: the total number of pamphlets printed by Mike and Leo.
    """
    # L1
    mike_speed_before_break = 600 # 600 pamphlets per hour
    mike_hours_before_break = 9 # 9 consecutive hours
    mike_pamphlets_before_break = mike_speed_before_break * mike_hours_before_break

    # L2
    speed_reduction_divisor = 3 # a third of the speed he was doing before
    mike_speed_after_break = mike_speed_before_break / speed_reduction_divisor

    # L3
    mike_hours_after_break = 2 # another 2 hours
    mike_pamphlets_after_break = mike_speed_after_break * mike_hours_after_break

    # L4
    leo_hours_divisor = 3 # a third as many hours as Mike did before his break
    leo_hours = mike_hours_before_break / leo_hours_divisor

    # L5
    leo_speed_multiplier = 2 # twice as fast as Mike before he took his break
    leo_speed = mike_speed_before_break * leo_speed_multiplier

    # L6
    leo_pamphlets = leo_speed * leo_hours

    # L7
    total_pamphlets = mike_pamphlets_before_break + mike_pamphlets_after_break + leo_pamphlets

    # FA
    answer = total_pamphlets
    return answer