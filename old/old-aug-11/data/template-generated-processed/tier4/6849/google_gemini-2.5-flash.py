def solve():
    """Index: 6849.
    Returns: the total trip duration in hours.
    """
    # L1
    minutes_per_rest_stop = 30 # 30-minute rest stops
    minutes_per_hour = 60 # WK
    rest_stop_duration_hours = minutes_per_rest_stop / minutes_per_hour

    # L3
    num_halves_of_trip = 2 # each half of the trip
    rest_time_per_half = 1 # two 30-minute rest stops during each half of the trip (2 * 0.5 hours = 1 hour)
    total_rest_time = num_halves_of_trip * rest_time_per_half

    # L4
    distance = 143 # 143 miles from Florence, Italy to Rome, Italy
    speed_with_load = 11 # 11 miles per hour as her top speed when she carries a typical load
    time_with_load = distance / speed_with_load

    # L5
    speed_without_load = 13 # 13 miles per hour when she is without any load to carry
    time_without_load = distance / speed_without_load

    # L6
    total_trip_duration = time_with_load + time_without_load + total_rest_time

    # FA
    answer = total_trip_duration
    return answer