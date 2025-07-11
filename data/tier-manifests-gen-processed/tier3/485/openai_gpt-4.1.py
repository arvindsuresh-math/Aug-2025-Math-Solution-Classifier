def solve():
    """Index: 485.
    Returns: the amount Lance makes on each workday.
    """
    # L1
    total_hours_per_week = 35 # Lance works 35 hours a week
    workdays_per_week = 5 # spread equally over 5 workdays
    hours_per_day = total_hours_per_week / workdays_per_week

    # L2
    hourly_wage = 9 # Lance earns $9 an hour
    daily_earnings = hourly_wage * hours_per_day

    # FA
    answer = daily_earnings
    return answer