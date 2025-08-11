def solve():
    """Index: 419.
    Returns: the number of hours Kenny practiced on the trumpet last week.
    """
    # L1
    basketball_hours = 10 # played 10 hours of basketball last week
    run_multiplier = 2 # ran for twice as long as he played basketball
    run_hours = basketball_hours * run_multiplier

    # L2
    trumpet_multiplier = 2 # practiced on the trumpet for twice as long as he ran
    trumpet_hours = run_hours * trumpet_multiplier

    # FA
    answer = trumpet_hours
    return answer