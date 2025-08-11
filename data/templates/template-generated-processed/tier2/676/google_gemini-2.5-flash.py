def solve():
    """Index: 676.
    Returns: the amount John pays for pills in a 30-day month.
    """
    # L1
    pills_per_day = 2 # 2 pills a day
    cost_per_pill = 1.5 # One pill costs $1.5
    daily_cost = pills_per_day * cost_per_pill

    # L2
    days_in_month = 30 # a 30-day month
    monthly_cost_before_insurance = daily_cost * days_in_month

    # L3
    insurance_coverage_percent = 0.4 # covers 40% of the cost
    insurance_coverage_amount = monthly_cost_before_insurance * insurance_coverage_percent

    # L4
    final_monthly_payment = monthly_cost_before_insurance - insurance_coverage_amount

    # FA
    answer = final_monthly_payment
    return answer