def solve():
    """Index: 4341.
    Returns: the total time it was raining in the three days.
    """
    # L1
    stop_time_day1 = 17 # stops at 17:00
    start_time_day1 = 7 # starts raining at 7:00
    rain_duration_day1 = stop_time_day1 - start_time_day1

    # L2
    extra_hours_day2 = 2 # takes 2 more hours
    rain_duration_day2 = rain_duration_day1 + extra_hours_day2

    # L3
    multiplier_day3 = 2 # twice the amount of time
    rain_duration_day3 = multiplier_day3 * rain_duration_day2

    # L4
    total_rain_time = rain_duration_day3 + rain_duration_day2 + rain_duration_day1

    # FA
    answer = total_rain_time
    return answer