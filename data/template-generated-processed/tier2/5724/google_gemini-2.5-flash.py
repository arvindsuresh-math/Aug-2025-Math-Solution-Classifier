def solve():
    """Index: 5724.
    Returns: the average speed Jason needs for the remainder of the drive.
    """
    # L1
    initial_speed = 60 # drives at 60 miles per hour
    initial_duration_hours = 0.5 # for 30 minutes
    initial_distance_driven = initial_speed * initial_duration_hours

    # L2
    total_distance = 120 # 120 miles away
    remaining_distance = total_distance - initial_distance_driven

    # L3
    total_time_decimal_hours = 1.5 # in exactly 1 hour 30 minutes
    remaining_time = total_time_decimal_hours - initial_duration_hours

    # L4
    required_average_speed = remaining_distance / remaining_time

    # FA
    answer = required_average_speed
    return answer