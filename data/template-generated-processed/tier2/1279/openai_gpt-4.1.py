def solve():
    """Index: 1279.
    Returns: the total amount Bill will spend for health insurance in a year.
    """
    # L1
    hourly_rate = 25 # $25/hour
    hours_per_week = 30 # 30 hours per week
    weekly_income = hourly_rate * hours_per_week

    # L2
    weeks_per_month = 4 # four weeks per month
    monthly_income = weekly_income * weeks_per_month

    # L3
    months_per_year = 12 # WK
    annual_income = monthly_income * months_per_year

    # L4
    monthly_premium = 500 # normal monthly price of the plan he wants is $500
    subsidy_percent = 0.5 # 50% if he makes between $10,001 and $40,000
    bill_monthly_cost = monthly_premium * subsidy_percent

    # L5
    annual_cost = bill_monthly_cost * months_per_year

    # FA
    answer = annual_cost
    return answer