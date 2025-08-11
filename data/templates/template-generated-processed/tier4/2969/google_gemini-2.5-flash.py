def solve():
    """Index: 2969.
    Returns: the cost per load of laundry in dollars.
    """
    # L1
    num_bottles = 2 # buys 2 bottles
    price_per_bottle_sale = 20.00 # drop to $20.00 a bottle
    total_cost_dollars = num_bottles * price_per_bottle_sale

    # L2
    loads_per_bottle = 80 # wash 80 loads of laundry
    total_loads = loads_per_bottle * num_bottles

    # L3
    cost_per_load_dollars = total_cost_dollars / total_loads

    # FA
    answer = cost_per_load_dollars
    return answer