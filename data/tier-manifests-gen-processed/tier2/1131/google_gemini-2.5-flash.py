def solve():
    """Index: 1131.
    Returns: the final cost for Juan to repair all four tires.
    """
    # L1
    num_tires = 4 # all 4 tires
    cost_per_tire = 7 # $7
    cost_tires_only = num_tires * cost_per_tire

    # L2
    sales_tax_per_tire = 0.50 # 50 cents
    total_sales_tax = sales_tax_per_tire * num_tires

    # L3
    final_cost = cost_tires_only + total_sales_tax

    # FA
    answer = final_cost
    return answer