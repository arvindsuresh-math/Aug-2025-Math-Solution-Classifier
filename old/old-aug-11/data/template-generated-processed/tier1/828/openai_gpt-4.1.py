def solve():
    """Index: 828.
    Returns: the total number of hours Tim slept over 4 days.
    """
    # L1
    days_first = 2 # 2 days in a row
    hours_first = 6 # 6 hours of sleep
    sleep_first = days_first * hours_first

    # L2
    days_next = 2 # the next 2 days
    hours_next = 10 # sleeps 10 hours
    sleep_next = days_next * hours_next

    # L3
    total_sleep = sleep_first + sleep_next

    # FA
    answer = total_sleep
    return answer