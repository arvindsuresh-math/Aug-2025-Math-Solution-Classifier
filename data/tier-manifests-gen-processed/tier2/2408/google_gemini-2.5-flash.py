def solve():
    """Index: 2408.
    Returns: Emmanuel's total charges for December.
    """
    # L1
    cost_per_day_international = 3.50 # $3.50 per day
    num_days_international = 10 # 10 days
    international_charge_cost = cost_per_day_international * num_days_international

    # L2
    regular_plan_cost_per_month = 175 # $175 per month for his regular plan
    total_bill_december = regular_plan_cost_per_month + international_charge_cost

    # FA
    answer = total_bill_december
    return answer