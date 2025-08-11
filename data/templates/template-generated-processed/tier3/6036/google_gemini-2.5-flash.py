def solve():
    """Index: 6036.
    Returns: the time the fish tank will be filled.
    """
    # L1
    initial_rainfall_first_hour = 2 # 2 inches of rainfall in the first hour
    rain_at_2pm = initial_rainfall_first_hour

    # L2
    duration_second_phase = 4 # For the next four hours
    rate_second_phase = 1 # 1 inch per hour
    rain_at_6pm = rain_at_2pm + duration_second_phase * rate_second_phase

    # L3
    tank_height = 18 # fish tank is 18 inches tall
    remaining_height_to_fill = tank_height - rain_at_6pm

    # L4
    rate_third_phase = 3 # three inches per hour
    hours_to_fill_remaining = remaining_height_to_fill / rate_third_phase

    # L5
    start_hour_third_phase = 6 # as of 6 pm
    fill_time_hour = start_hour_third_phase + hours_to_fill_remaining

    # FA
    answer = fill_time_hour
    return answer