def solve():
    """Index: 1298.
    Returns: the total time the plane hovered over Mountain, Central, and Eastern time zones in two days.
    """
    # L1
    mountain_time_day1 = 3 # hovered in Mountain time for 3 hours
    central_time_day1 = 4 # Central time for 4 hrs
    total_mountain_central_day1 = mountain_time_day1 + central_time_day1

    # L2
    eastern_time_day1 = 2 # Eastern time for 2 hrs
    total_day1 = total_mountain_central_day1 + eastern_time_day1

    # L3
    extra_hours_each = 2 # 2 more hours to hover in each of the places
    num_places = 3 # Mountain, Central, Eastern
    extra_total_day2 = extra_hours_each * num_places

    # L4
    total_day2 = total_day1 + extra_total_day2

    # L5
    total_hover_time = total_day2 + total_day1

    # FA
    answer = total_hover_time
    return answer