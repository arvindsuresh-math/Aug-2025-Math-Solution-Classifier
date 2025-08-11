def solve():
    """Index: 3553.
    Returns: the amount of water left in the pool.
    """
    # L1
    pool_capacity_liters = 120 # The pool holds 120 liters of water
    drain_time_hours = 4 # drain can empty the pool in 4 hours
    drain_rate_liters_per_hour = pool_capacity_liters / drain_time_hours

    # L2
    time_elapsed_hours = 3 # after 3 hours
    water_drained_liters = time_elapsed_hours * drain_rate_liters_per_hour

    # L3
    hose_fill_time_hours = 6 # hose can fill the pool in 6 hours
    hose_fill_rate_liters_per_hour = pool_capacity_liters / hose_fill_time_hours

    # L4
    water_added_liters = time_elapsed_hours * hose_fill_rate_liters_per_hour

    # L5
    water_left_liters = pool_capacity_liters + water_added_liters - water_drained_liters

    # FA
    answer = water_left_liters
    return answer