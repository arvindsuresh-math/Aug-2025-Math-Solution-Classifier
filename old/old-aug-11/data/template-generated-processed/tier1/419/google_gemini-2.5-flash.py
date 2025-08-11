def solve():
    """Index: 419.
    Returns: the number of hours Kenny practiced on the trumpet last week.
    """
    # L1
    basketball_hours = 10 # 10 hours of basketball last week
    multiplier_running = 2 # twice as long as he played basketball
    running_hours = basketball_hours * multiplier_running

    # L2
    multiplier_trumpet = 2 # twice as long as he ran
    trumpet_hours = running_hours * multiplier_trumpet

    # FA
    answer = trumpet_hours
    return answer