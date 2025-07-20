def solve():
    """Index: 4295.
    Returns: the total time it will take to reach New York.
    """
    # L1
    total_distance = 300 # Jessica's family is 300 km away
    travel_speed = 50 # traveling at the rate of 50 km/h
    travel_time_no_rest = total_distance / travel_speed

    # L2
    travel_interval_before_rest = 2 # every 2 hours
    num_intervals = travel_time_no_rest / travel_interval_before_rest
    number_of_rests = num_intervals - 1

    # L3
    rest_duration_minutes = 30 # rest for 30 minutes
    total_rest_minutes = number_of_rests * rest_duration_minutes
    minutes_per_hour = 60 # WK
    total_rest_hours = total_rest_minutes / minutes_per_hour

    # L4
    total_travel_time = travel_time_no_rest + total_rest_hours

    # FA
    answer = total_travel_time
    return answer