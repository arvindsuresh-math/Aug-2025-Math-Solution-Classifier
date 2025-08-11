def solve():
    """Index: 4715.
    Returns: Mary's total garbage bill.
    """
    # L1
    cost_per_trash_bin = 10 # $10 per trash bin
    num_trash_bins = 2 # 2 trash bins
    weekly_trash_cost = cost_per_trash_bin * num_trash_bins

    # L2
    cost_per_recycling_bin = 5 # $5 per recycling bin
    weekly_total_cost = weekly_trash_cost + cost_per_recycling_bin

    # L3
    weeks_per_month = 4 # exactly four weeks
    monthly_base_cost = weekly_total_cost * weeks_per_month

    # L4
    discount_percent_num = 18 # 18% discount
    percent_factor = 0.01 # WK
    senior_discount_amount = discount_percent_num * percent_factor * monthly_base_cost

    # L5
    fine_amount = 20 # $20 fine
    total_monthly_cost = monthly_base_cost - senior_discount_amount + fine_amount

    # FA
    answer = total_monthly_cost
    return answer