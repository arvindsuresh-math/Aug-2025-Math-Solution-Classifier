def solve():
    """Index: 5888.
    Returns: Julie's monthly salary after missing one day of work.
    """
    # L1
    hourly_rate = 5 # hourly rate of $5
    hours_per_day = 8 # works 8 hours a day
    daily_earnings = hourly_rate * hours_per_day

    # L2
    days_per_week = 6 # 6 days a week
    weekly_earnings = daily_earnings * days_per_week

    # L3
    weeks_per_month = 4 # WK
    monthly_earnings_full = weekly_earnings * weeks_per_month

    # L4
    monthly_salary_adjusted = monthly_earnings_full - daily_earnings

    # FA
    answer = monthly_salary_adjusted
    return answer