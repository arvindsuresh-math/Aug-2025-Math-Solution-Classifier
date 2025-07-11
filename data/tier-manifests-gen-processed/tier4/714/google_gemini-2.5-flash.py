def solve():
    """Index: 714.
    Returns: the amount John makes per day.
    """
    # L1
    total_monthly_visits = 30000 # 30000 visits a month
    normal_month_days = 30 # normal 30 day month
    visits_per_day = total_monthly_visits / normal_month_days

    # L2
    earnings_per_visit = 0.01 # $.01 per visit
    earnings_per_day = visits_per_day * earnings_per_visit

    # FA
    answer = earnings_per_day
    return answer