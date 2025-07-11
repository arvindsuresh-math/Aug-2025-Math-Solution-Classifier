def solve():
    """Index: 1985.
    Returns: the time it takes to fill the basin in seconds.
    """
    # L1
    water_inflow_rate = 24 # 24 gallons per second of water flows down a waterfall
    water_leak_rate = 4 # leaks water at 4 gallons per second
    net_flow_rate = water_inflow_rate - water_leak_rate

    # L2
    basin_capacity = 260 # basin that can hold 260 gallons of water
    time_to_fill = basin_capacity / net_flow_rate

    # FA
    answer = time_to_fill
    return answer