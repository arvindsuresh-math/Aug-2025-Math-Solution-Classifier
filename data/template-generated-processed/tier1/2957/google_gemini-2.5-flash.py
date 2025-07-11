def solve():
    """Index: 2957.
    Returns: the total sleep Tim gets per week.
    """
    # L1
    sleep_hours_first_period = 6 # 6 hours per day
    days_first_period = 5 # 5 days a week
    total_sleep_first_period = sleep_hours_first_period * days_first_period

    # L2
    sleep_hours_second_period = 10 # 10 hours a day
    days_second_period = 2 # other 2
    total_sleep_second_period = sleep_hours_second_period * days_second_period

    # L3
    total_sleep = total_sleep_first_period + total_sleep_second_period

    # FA
    answer = total_sleep
    return answer