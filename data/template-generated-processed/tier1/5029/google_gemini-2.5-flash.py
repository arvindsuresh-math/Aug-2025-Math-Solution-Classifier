def solve():
    """Index: 5029.
    Returns: the amount of money left in Maria's savings after buying all items.
    """
    # L1
    sweater_price = 30 # sells handmade sweaters for $30
    num_sweaters = 6 # buy 6 sweaters
    total_sweater_cost = sweater_price * num_sweaters

    # L2
    scarf_price = 20 # handmade scarf for $20
    num_scarves = 6 # buy 6 scarves
    total_scarf_cost = scarf_price * num_scarves

    # L3
    total_cost = total_sweater_cost + total_scarf_cost

    # L4
    initial_savings = 500 # has saved $500
    remaining_savings = initial_savings - total_cost

    # FA
    answer = remaining_savings
    return answer