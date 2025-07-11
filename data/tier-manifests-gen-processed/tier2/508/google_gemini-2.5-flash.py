def solve():
    """Index: 508.
    Returns: the total distance James drove.
    """
    # L1
    first_speed = 30 # James drives 30 mph
    first_duration = 0.5 # for half an hour
    first_distance = first_speed * first_duration

    # L2
    second_duration = first_duration * 2

    # L3
    second_speed = first_speed * 2

    # L4
    second_distance = second_speed * second_duration

    # L5
    total_distance = second_distance + first_distance

    # FA
    answer = total_distance
    return answer