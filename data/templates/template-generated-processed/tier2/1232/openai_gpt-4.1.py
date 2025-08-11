def solve():
    """Index: 1232.
    Returns: Megan's total earnings for two months of work.
    """
    # L1
    hours_per_day = 8 # works eight hours a day
    wage_per_hour = 7.5 # earns $7.50 per hour
    daily_earnings = hours_per_day * wage_per_hour

    # L2
    days_per_month = 20 # works 20 days a month
    monthly_earnings = days_per_month * daily_earnings

    # L3
    num_months = 2 # two months of work
    total_earnings = num_months * monthly_earnings

    # FA
    answer = total_earnings
    return answer