def solve():
    """Index: 2901.
    Returns: the total time the process takes.
    """
    # L1
    distance_walked = 64 # 64 feet
    walking_rate = 8 # 8 feet/minute
    walking_time = distance_walked / walking_rate

    # L2
    resisting_time = 20 # twenty minutes resisting
    total_time = walking_time + resisting_time

    # FA
    answer = total_time
    return answer