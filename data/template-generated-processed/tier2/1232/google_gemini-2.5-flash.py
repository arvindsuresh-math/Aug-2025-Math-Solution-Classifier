def solve():
    """Index: 1232.
    Returns: Megan's total earnings for two months of work.
    """
    # L1
    hours_per_day = 8 # eight hours a day
    hourly_wage = 7.50 # earns $7.50 per hour
    daily_earnings = hours_per_day * hourly_wage

    # L2
    work_days_per_month = 20 # works 20 days a month
    monthly_earnings = work_days_per_month * daily_earnings

    # L3
    number_of_months = 2 # two months of work
    total_earnings = number_of_months * monthly_earnings

    # FA
    answer = total_earnings
    return answer