def solve():
    """Index: 7161.
    Returns: the number of hours Kenny played basketball.
    """
    # L1
    trumpet_practice_hours = 40 # practiced on the trumpet for 40 hours
    run_divisor = 2 # practiced on the trumpet for twice as long as he ran
    hours_ran = trumpet_practice_hours / run_divisor

    # L2
    basketball_divisor = 2 # ran for twice as long as he played basketball
    basketball_hours = hours_ran / basketball_divisor

    # FA
    answer = basketball_hours
    return answer