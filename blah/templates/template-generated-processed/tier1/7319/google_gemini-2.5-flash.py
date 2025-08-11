def solve():
    """Index: 7319.
    Returns: the time it would take to reach the destination at the new speed.
    """
    # L1
    time_taken_initial = 4 # 4 hours to reach a destination
    speed_initial = 50 # 50 miles per hour
    distance = time_taken_initial * speed_initial

    # L2
    speed_new = 100 # 100 miles per hour
    time_taken_new = distance / speed_new

    # FA
    answer = time_taken_new
    return answer