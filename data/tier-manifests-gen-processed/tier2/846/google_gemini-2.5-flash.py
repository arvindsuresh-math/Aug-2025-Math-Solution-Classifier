def solve():
    """Index: 846.
    Returns: the amount of money Kurt saves in a 30-day month.
    """
    # L1
    old_refrigerator_daily_cost = 0.85 # cost $0.85 a day
    month_duration_days = 30 # 30-day month
    old_refrigerator_monthly_cost = old_refrigerator_daily_cost * month_duration_days

    # L2
    new_refrigerator_daily_cost = 0.45 # cost $0.45 a day
    new_refrigerator_monthly_cost = new_refrigerator_daily_cost * month_duration_days

    # L3
    monthly_savings = old_refrigerator_monthly_cost - new_refrigerator_monthly_cost

    # FA
    answer = monthly_savings
    return answer