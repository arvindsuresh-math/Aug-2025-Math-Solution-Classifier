def solve():
    """Index: 6996.
    Returns: the net increase in Bob's weekly earnings.
    """
    # L1
    raise_per_hour = 0.50 # $0.50/hour
    hours_per_week = 40 # works 40 hours a week
    weekly_raise_earnings = raise_per_hour * hours_per_week

    # L2
    monthly_benefit_reduction = 60 # reduced by $60/month
    weeks_per_month = 4 # WK
    weekly_benefit_reduction = monthly_benefit_reduction / weeks_per_month

    # L3
    net_weekly_increase = weekly_raise_earnings - weekly_benefit_reduction

    # FA
    answer = net_weekly_increase
    return answer