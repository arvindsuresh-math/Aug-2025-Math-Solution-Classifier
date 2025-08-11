def solve():
    """Index: 2025.
    Returns: the number of buses that leave the station in 5 days.
    """
    # L1
    buses_per_half_hour = 1 # a bus leaves every half-hour
    half_hours_per_hour = 2 # WK (2 half-hours in an hour)
    buses_per_hour = buses_per_half_hour + buses_per_half_hour

    # L2
    hours_per_day = 12 # 12 hours a day
    num_days = 5 # 5 days
    total_buses = buses_per_hour * hours_per_day * num_days

    # FA
    answer = total_buses
    return answer