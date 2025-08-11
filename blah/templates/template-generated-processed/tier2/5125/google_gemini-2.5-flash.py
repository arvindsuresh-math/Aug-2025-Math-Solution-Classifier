def solve():
    """Index: 5125.
    Returns: the total kilometers Mercedes and Davonte ran.
    """
    # L1
    jonathan_distance = 7.5 # Jonathan ran 7.5 kilometers
    twice_factor = 2 # twice that distance
    mercedes_distance = twice_factor * jonathan_distance

    # L2
    davonte_extra_distance = 2 # 2 kilometers farther
    davonte_distance = mercedes_distance + davonte_extra_distance

    # L3
    total_distance = mercedes_distance + davonte_distance

    # FA
    answer = total_distance
    return answer