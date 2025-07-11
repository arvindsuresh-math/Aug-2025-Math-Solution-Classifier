def solve():
    """Index: 1930.
    Returns: the amount of water left after dumping half.
    """
    # L1
    flow_rate_cups_per_interval = 2 # 2 cups per 10 minutes
    interval_minutes = 10 # 2 cups per 10 minutes
    first_period_minutes = 30 # first 30 minutes
    num_intervals_first_period = first_period_minutes / interval_minutes
    water_first_period = num_intervals_first_period * flow_rate_cups_per_interval

    # L2
    next_period_minutes = 30 # next 30 minutes
    num_intervals_next_period = next_period_minutes / interval_minutes
    water_next_period = num_intervals_next_period * flow_rate_cups_per_interval

    # L3
    max_flow_rate_cups_per_interval = 4 # 4 cups per 10 minutes
    max_flow_period_hours = 1 # For the next hour
    minutes_per_hour = 60 # WK
    max_flow_period_minutes = max_flow_period_hours * minutes_per_hour
    num_intervals_max_flow = max_flow_period_minutes / interval_minutes
    water_max_flow_period = num_intervals_max_flow * max_flow_rate_cups_per_interval

    # L4
    total_water_came_out = water_first_period + water_next_period + water_max_flow_period

    # L5
    dump_divisor = 2 # dump half of the water away
    water_left = total_water_came_out / dump_divisor

    # FA
    answer = water_left
    return answer