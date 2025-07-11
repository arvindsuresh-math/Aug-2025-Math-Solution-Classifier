def solve():
    """Index: 1279.
    Returns: the annual cost Bill will spend for health insurance.
    """
    # L1
    hourly_rate = 25 # Bill earns $25/hour
    hours_per_week = 30 # works 30 hours per week
    weekly_earnings = hourly_rate * hours_per_week

    # L2
    weeks_per_month = 4 # four weeks per month
    monthly_earnings = weekly_earnings * weeks_per_month

    # L3
    months_per_year = 12 # WK
    annual_income = monthly_earnings * months_per_year

    # L4
    normal_monthly_price = 500 # normal monthly price of the plan he wants is $500
    subsidy_percent_decimal = 0.5 # 50% if he makes between $10,001 and $40,000
    bill_monthly_cost = normal_monthly_price * subsidy_percent_decimal

    # L5
    bill_annual_cost = bill_monthly_cost * months_per_year

    # FA
    answer = bill_annual_cost
    return answer