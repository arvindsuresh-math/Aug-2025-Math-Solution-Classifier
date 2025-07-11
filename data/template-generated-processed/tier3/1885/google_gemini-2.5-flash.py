def solve():
    """Index: 1885.
    Returns: the number of hours it will take Michael to dig his hole.
    """
    # L1
    father_rate_feet_per_hour = 4 # rate of 4 feet per hour
    father_hours = 400 # father took 400 hours
    father_hole_depth = father_rate_feet_per_hour * father_hours

    # L2
    twice_multiplier = 2 # twice the depth
    twice_father_depth = twice_multiplier * father_hole_depth

    # L3
    less_depth = 400 # 400 feet less deep
    michael_target_depth = twice_father_depth - less_depth

    # L4
    michael_rate_feet_per_hour = 4 # working at the same rate
    michael_hours = michael_target_depth / michael_rate_feet_per_hour

    # FA
    answer = michael_hours
    return answer