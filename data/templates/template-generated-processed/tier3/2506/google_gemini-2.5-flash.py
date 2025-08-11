def solve():
    """Index: 2506.
    Returns: the total hours of sleep Tom gets per night.
    """
    # L1
    initial_sleep_hours = 6 # 6 hours of sleep a day
    increase_denominator = 3 # by 1/3
    increased_sleep_amount = initial_sleep_hours / increase_denominator

    # L2
    total_sleep_hours = initial_sleep_hours + increased_sleep_amount

    # FA
    answer = total_sleep_hours
    return answer