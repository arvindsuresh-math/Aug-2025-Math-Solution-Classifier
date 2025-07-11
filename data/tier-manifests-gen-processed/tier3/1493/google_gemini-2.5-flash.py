def solve():
    """Index: 1493.
    Returns: the total number of hours traveled.
    """
    # L3
    initial_distance = 100 # first 100 miles
    initial_time = 1 # 1 hour
    second_distance = 300 # 300 miles
    time_for_second_part = second_distance * initial_time / initial_distance

    # L5
    total_travel_time = time_for_second_part + initial_time

    # FA
    answer = total_travel_time
    return answer