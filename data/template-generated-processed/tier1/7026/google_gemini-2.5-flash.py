def solve():
    """Index: 7026.
    Returns: Alton's total profit every week.
    """
    # L1
    daily_earnings = 8 # $8 per day
    days_per_week = 7 # WK
    weekly_earnings = daily_earnings * days_per_week

    # L2
    weekly_rent_cost = 20 # $20 per week
    weekly_profit = weekly_earnings - weekly_rent_cost

    # FA
    answer = weekly_profit
    return answer