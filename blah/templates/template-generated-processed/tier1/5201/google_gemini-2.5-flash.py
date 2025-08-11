def solve():
    """Index: 5201.
    Returns: the total time, in minutes, that Kira takes to travel between the first and third station.
    """
    # L1
    hours_between_stations = 2 # 2 hours apart from one another
    travel_hours = hours_between_stations + hours_between_stations

    # L2
    minutes_per_hour = 60 # WK
    travel_minutes = travel_hours * minutes_per_hour

    # L3
    break_minutes = 30 # taking a 30 minutes break
    total_time_with_break = travel_minutes + break_minutes

    # FA
    answer = total_time_with_break
    return answer