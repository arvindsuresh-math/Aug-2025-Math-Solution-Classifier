def solve():
    """Index: 2025.
    Returns: the total number of buses that leave the station over 5 days.
    """
    # L1
    buses_in_first_half_hour = 1 # WK
    buses_in_second_half_hour = 1 # WK
    buses_per_hour = buses_in_first_half_hour + buses_in_second_half_hour

    # L2
    hours_per_day = 12 # 12 hours a day
    num_days = 5 # for 5 days
    total_buses = buses_per_hour * hours_per_day * num_days

    # FA
    answer = total_buses
    return answer