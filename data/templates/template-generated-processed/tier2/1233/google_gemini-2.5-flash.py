def solve():
    """Index: 1233.
    Returns: the total distance Kevin ran in miles.
    """
    # L1
    first_speed = 10 # ran at 10 miles per hour
    first_duration = 0.5 # for half an hour
    first_distance = first_speed * first_duration

    # L2
    second_speed = 20 # 20 miles per hour
    second_duration = 0.5 # for half an hour
    second_distance = second_speed * second_duration

    # L3
    third_speed = 8 # ran at 8 miles per hour
    third_duration_hours = 0.25 # for 15 minutes
    third_distance = third_speed * third_duration_hours

    # L4
    total_distance = first_distance + second_distance + third_distance

    # FA
    answer = total_distance
    return answer