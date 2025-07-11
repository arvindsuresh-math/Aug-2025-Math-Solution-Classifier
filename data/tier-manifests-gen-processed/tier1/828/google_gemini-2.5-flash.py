def solve():
    """Index: 828.
    Returns: the total amount of sleep Tim got.
    """
    # L1
    num_days_initial = 2 # 2 days in a row
    sleep_hours_initial_day = 6 # 6 hours of sleep
    sleep_initial_days = num_days_initial * sleep_hours_initial_day

    # L2
    num_days_next = 2 # the next 2 days
    sleep_hours_next_day = 10 # 10 hours the next 2 days
    sleep_next_days = num_days_next * sleep_hours_next_day

    # L3
    total_sleep = sleep_initial_days + sleep_next_days

    # FA
    answer = total_sleep
    return answer