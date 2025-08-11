def solve():
    """Index: 3179.
    Returns: the amount of change Celine gets back.
    """
    # L1
    num_laptops = 2 # two laptops
    laptop_price = 600 # laptops at $600 each
    cost_laptops = num_laptops * laptop_price

    # L2
    num_smartphones = 4 # four smartphones
    smartphone_price = 400 # smartphone at $400
    cost_smartphones = num_smartphones * smartphone_price

    # L3
    total_cost = cost_laptops + cost_smartphones

    # L4
    money_had = 3000 # she has $3000
    change = money_had - total_cost

    # FA
    answer = change
    return answer