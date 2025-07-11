def solve():
    """Index: 1646.
    Returns: the number of passengers that fit in 5 buses.
    """
    # L1
    total_passengers = 198 # 198 passengers
    total_buses = 9 # 9 buses
    passengers_per_bus = total_passengers / total_buses

    # L2
    target_buses = 5 # 5 buses
    passengers_in_target_buses = passengers_per_bus * target_buses

    # FA
    answer = passengers_in_target_buses
    return answer