def solve():
    """Index: 3310.
    Returns: the number of additional gallons needed to fill the tank.
    """
    # L1
    pour_time_minutes = 6 # for 6 minutes
    seconds_per_minute = 60 # WK
    total_time_seconds = pour_time_minutes * seconds_per_minute

    # L2
    time_per_gallon = 20 # 1 gallon every 20 seconds
    gallons_per_interval = 1 # 1 gallon every 20 seconds
    gallons_poured = total_time_seconds / time_per_gallon / gallons_per_interval

    # L3
    tank_capacity = 50 # 50-gallon fish tank
    gallons_needed = tank_capacity - gallons_poured

    # FA
    answer = gallons_needed
    return answer