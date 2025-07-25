def solve():
    """Index: 3157.
    Returns: the number of GB Chris was charged for over the base amount.
    """
    # L2
    cost_per_gb_over = 0.25 # $0.25 for every 1 GB over
    base_rate = 45 # $45 per month
    total_bill = 65 # His bill for this month is $65
    cost_of_overage = total_bill - base_rate

    # L4
    gb_over_charged = cost_of_overage / cost_per_gb_over

    # FA
    answer = gb_over_charged
    return answer