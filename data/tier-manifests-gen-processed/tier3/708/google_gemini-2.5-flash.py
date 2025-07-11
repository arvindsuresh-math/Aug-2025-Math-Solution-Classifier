def solve():
    """Index: 708.
    Returns: the time it takes to fill the tub in minutes.
    """
    # L1
    flow_rate_per_minute = 12 # The flow rate of the tap is 12 liters per minute
    leak_rate_per_minute = 1 # lets 1 liter of water escape per minute
    on_time_per_cycle = 1 # letting the water run for 1 minute
    off_time_per_cycle = 1 # closing the water supply for 1 minute
    cycle_duration = on_time_per_cycle + off_time_per_cycle
    water_flowed_in_cycle = flow_rate_per_minute * on_time_per_cycle
    water_escaped_cycle = leak_rate_per_minute * cycle_duration

    # L2
    net_gain_per_cycle = water_flowed_in_cycle - water_escaped_cycle

    # L3
    average_flow_rate = net_gain_per_cycle / cycle_duration

    # L4
    tub_capacity = 120 # fill a 120-liter tub
    time_to_fill_tub = tub_capacity / average_flow_rate

    # FA
    answer = time_to_fill_tub
    return answer