def solve():
    """Index: 6250.
    Returns: the total miles Bob traveled.
    """
    # L1
    first_duration = 1.5 # one and a half hours
    first_speed = 60 # 60/mph
    first_distance = first_duration * first_speed

    # L2
    second_duration = 2 # 2 hours
    second_speed = 45 # 45/mph
    second_distance = second_duration * second_speed

    # L3
    total_distance = first_distance + second_distance

    # FA
    answer = total_distance
    return answer