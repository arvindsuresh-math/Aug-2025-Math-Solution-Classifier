def solve():
    """Index: 1131.
    Returns: the final cost for repairing all 4 tires including sales tax.
    """
    # L1
    num_tires = 4 # all 4 tires
    repair_cost_per_tire = 7 # repair for each tire costs $7
    total_repair_cost = num_tires * repair_cost_per_tire

    # L2
    sales_tax_per_tire = 0.50 # another 50 cents for sales tax
    total_sales_tax = sales_tax_per_tire * num_tires

    # L3
    total_cost = total_repair_cost + total_sales_tax

    # FA
    answer = total_cost
    return answer