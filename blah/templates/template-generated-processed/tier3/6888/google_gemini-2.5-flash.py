def solve():
    """Index: 6888.
    Returns: the additional cost of a pint of strawberries when not on sale.
    """
    # L1
    sale_revenue = 216 # made $216
    pints_sold = 54 # sold 54 pints
    cost_per_pint_on_sale = sale_revenue / pints_sold

    # L2
    less_than_no_sale = 108 # $108 less than they would have made
    revenue_no_sale = sale_revenue + less_than_no_sale

    # L3
    cost_per_pint_no_sale = revenue_no_sale / pints_sold

    # L4
    additional_cost = cost_per_pint_no_sale - cost_per_pint_on_sale

    # FA
    answer = additional_cost
    return answer