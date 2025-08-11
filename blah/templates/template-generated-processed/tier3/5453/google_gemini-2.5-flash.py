def solve():
    """Index: 5453.
    Returns: the total hours Bryan spends traveling per year.
    """
    # L1
    walk_to_bus_minutes = 5 # 5 minutes to walk from his house to the bus station
    bus_ride_minutes = 20 # rides the bus for 20 minutes
    walk_from_bus_minutes = 5 # walks 5 minutes from the bus station to his job
    travel_to_work_minutes = walk_to_bus_minutes + bus_ride_minutes + walk_from_bus_minutes

    # L2
    times_per_day = 2 # twice a day
    daily_travel_minutes = travel_to_work_minutes * times_per_day

    # L3
    minutes_per_hour = 60 # WK
    daily_travel_hours = daily_travel_minutes / minutes_per_hour

    # L4
    days_per_year = 365 # WK
    annual_travel_hours = daily_travel_hours * days_per_year

    # FA
    answer = annual_travel_hours
    return answer