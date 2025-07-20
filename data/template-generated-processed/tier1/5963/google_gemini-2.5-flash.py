def solve():
    """Index: 5963.
    Returns: the price of the coffee table.
    """
    # L1
    armchair_cost_each = 425 # 2 armchairs costing $425 each
    num_armchairs = 2 # 2 armchairs
    total_armchair_cost = armchair_cost_each * num_armchairs

    # L2
    total_invoice_amount = 2430 # The total amount of the invoice is $2,430
    sofa_cost = 1250 # a sofa worth $1,250
    intermediate_sum = sofa_cost + total_armchair_cost
    coffee_table_price = total_invoice_amount - intermediate_sum

    # FA
    answer = coffee_table_price
    return answer