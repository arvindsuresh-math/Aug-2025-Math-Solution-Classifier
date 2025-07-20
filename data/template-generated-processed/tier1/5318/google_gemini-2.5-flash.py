def solve():
    """Index: 5318.
    Returns: the amount of money Casey saves by paying monthly.
    """
    # L1
    num_months = 3 # 3 months
    weeks_per_month = 4 # 4 weeks
    total_weeks = num_months * weeks_per_month

    # L2
    weekly_rate = 280 # $280/week
    cost_weekly = total_weeks * weekly_rate

    # L3
    monthly_rate = 1000 # $1000/month
    cost_monthly = monthly_rate * num_months

    # L4
    savings = cost_weekly - cost_monthly

    # FA
    answer = savings
    return answer