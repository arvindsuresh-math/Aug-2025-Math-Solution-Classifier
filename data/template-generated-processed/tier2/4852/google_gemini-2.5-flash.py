def solve():
    """Index: 4852.
    Returns: the amount paid for the annual subscription.
    """
    # L1
    months_per_year = 12 # WK
    cost_per_month = 10 # newspaper subscription costs $10/month
    cost_per_year_no_discount = months_per_year * cost_per_month

    # L2
    discount_percent = 20 # 20% discount
    percent_factor = 0.01 # WK
    final_annual_cost = cost_per_year_no_discount * (1 - discount_percent * percent_factor)

    # FA
    answer = final_annual_cost
    return answer