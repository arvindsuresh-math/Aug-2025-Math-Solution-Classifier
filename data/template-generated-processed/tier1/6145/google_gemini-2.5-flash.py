def solve():
    """Index: 6145.
    Returns: the extra time it takes to fill 12 barrels with a leak.
    """
    # L1
    normal_fill_time_per_barrel = 3 # 3 minutes
    num_barrels = 12 # 12 barrels of soda
    normal_total_time = normal_fill_time_per_barrel * num_barrels

    # L2
    leak_fill_time_per_barrel = 5 # took 5 minutes to fill one barrel
    leak_total_time = leak_fill_time_per_barrel * num_barrels

    # L3
    extra_time = leak_total_time - normal_total_time

    # FA
    answer = extra_time
    return answer