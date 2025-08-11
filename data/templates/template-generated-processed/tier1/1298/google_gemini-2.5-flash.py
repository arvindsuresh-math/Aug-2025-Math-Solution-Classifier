def solve():
    """Index: 1298.
    Returns: the total time the plane hovered over the places in the two days.
    """
    # L1
    mountain_time_initial = 3 # hovered in Mountain time for 3 hours
    central_time_initial = 4 # Central time for 4 hrs
    mountain_central_time_initial = mountain_time_initial + central_time_initial

    # L2
    eastern_time_initial = 2 # Eastern time for 2 hrs
    total_time_day1 = mountain_central_time_initial + eastern_time_initial

    # L3
    extra_hours_per_place = 2 # 2 more hours to hover in each of the places
    num_places = 3 # each of the places it passed through the previous day (Mountain, Central, Eastern)
    extra_time_day2 = extra_hours_per_place * num_places

    # L4
    total_time_day2 = total_time_day1 + extra_time_day2

    # L5
    total_hover_time_two_days = total_time_day2 + total_time_day1

    # FA
    answer = total_hover_time_two_days
    return answer