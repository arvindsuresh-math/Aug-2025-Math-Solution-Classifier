def solve():
    """Index: 4830.
    Returns: the total time Martha spent on these activities.
    """
    # L1
    router_time = 10 # 10 minutes turning the router off and on again
    hold_multiplier = 6 # six times that long on hold
    hold_time = router_time * hold_multiplier

    # L2
    yelling_divisor = 2 # half as much time as she spent on hold yelling
    yelling_time = hold_time / yelling_divisor

    # L3
    total_time = hold_time + yelling_time + router_time

    # FA
    answer = total_time
    return answer