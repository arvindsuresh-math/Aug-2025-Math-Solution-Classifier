def solve():
    """Index: 2969.
    Returns: the cost in cents per load of laundry if Frank buys 2 bottles of detergent.
    """
    # L1
    num_bottles = 2 # If he buys 2 bottles
    sale_price_per_bottle = 20.00 # price drops to $20.00 per bottle
    total_cost_dollars = num_bottles * sale_price_per_bottle

    # L2
    loads_per_bottle = 80 # 80 loads of laundry per bottle
    total_loads = loads_per_bottle * num_bottles

    # L3
    cost_per_load_dollars = total_cost_dollars / total_loads
    cents_per_dollar = 100 # WK
    cost_per_load_cents = cost_per_load_dollars * cents_per_dollar

    # FA
    answer = cost_per_load_cents
    return answer