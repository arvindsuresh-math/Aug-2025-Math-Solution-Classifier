def solve():
    """Index: 485.
    Returns: the amount Lance makes on each workday.
    """
    # L1
    weekly_hours = 35 # He works 35 hours a week
    workdays_per_week = 5 # spread equally over 5 workdays
    hours_per_day = weekly_hours / workdays_per_week

    # L2
    hourly_rate = 9 # Lance earns $9 an hour
    earnings_per_workday = hourly_rate * hours_per_day

    # FA
    answer = earnings_per_workday
    return answer