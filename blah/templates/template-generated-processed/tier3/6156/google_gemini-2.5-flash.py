def solve():
    """Index: 6156.
    Returns: the required speed for the next 2 hours.
    """
    # L1
    target_average_speed = 70 # average speed of 70 mph
    total_time_needed = 5 # over the next 2 hours to get an average speed of 70 mph
    total_distance_needed = target_average_speed * total_time_needed

    # L2
    initial_speed = 60 # drives 60 mph
    initial_time = 3 # for 3 hours
    initial_distance_traveled = initial_speed * initial_time

    # L3
    remaining_distance = total_distance_needed - initial_distance_traveled

    # L4
    remaining_time = 2 # over the next 2 hours
    required_speed = remaining_distance / remaining_time

    # FA
    answer = required_speed
    return answer