def solve():
    """Index: 5847.
    Returns: Ursula's annual salary.
    """
    # L1
    hours_per_day = 8 # She works 8 hours a day
    hourly_wage = 8.50 # earns $8.50 an hour
    daily_earnings = hours_per_day * hourly_wage

    # L2
    work_days_per_month = 20 # works 20 days a month
    monthly_earnings = work_days_per_month * daily_earnings

    # L3
    months_per_year = 12 # WK
    annual_salary = months_per_year * monthly_earnings

    # FA
    answer = annual_salary
    return answer