def solve():
    """Index: 714.
    Returns: the amount John makes per day.
    """
    # L1
    monthly_visits = 30000 # 30000 visits a month
    days_in_month = 30 # 30 day month
    daily_visits = monthly_visits / days_in_month

    # L2
    earnings_per_visit = 0.01 # $.01 per visit
    daily_earnings = daily_visits * earnings_per_visit

    # FA
    answer = daily_earnings
    return answer