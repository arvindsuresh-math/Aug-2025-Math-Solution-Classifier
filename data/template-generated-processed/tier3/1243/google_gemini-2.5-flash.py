def solve():
    """Index: 1243.
    Returns: the distance the jet could fly in 10 hours.
    """
    # L1
    distance_initial = 580 # 580 miles
    time_initial = 2 # 2 hours
    speed = distance_initial / time_initial

    # L2
    target_time = 10 # in 10 hours
    distance_final = speed * target_time

    # FA
    answer = distance_final
    return answer