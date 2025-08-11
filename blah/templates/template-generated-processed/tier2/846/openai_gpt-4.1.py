def solve():
    """Index: 846.
    Returns: the amount of money Kurt saves in a 30-day month with his new refrigerator.
    """
    # L1
    old_daily_cost = 0.85 # old refrigerator cost $0.85 a day
    num_days = 30 # 30-day month
    old_monthly_cost = old_daily_cost * num_days

    # L2
    new_daily_cost = 0.45 # new refrigerator cost $0.45 a day
    new_monthly_cost = new_daily_cost * num_days

    # L3
    savings = old_monthly_cost - new_monthly_cost

    # FA
    answer = savings
    return answer