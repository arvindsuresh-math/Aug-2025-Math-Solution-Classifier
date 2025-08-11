def solve():
    """Index: 4029.
    Returns: the number of ice-pops that must be sold.
    """
    # L1
    num_pencils = 100 # 100 pencils
    cost_per_pencil = 1.80 # $1.80 each
    total_pencil_cost = num_pencils * cost_per_pencil

    # L2
    sell_price_per_pop = 1.50 # $1.50
    cost_to_make_per_pop = 0.90 # 90 cents
    profit_per_pop = sell_price_per_pop - cost_to_make_per_pop

    # L3
    num_pops_to_sell = total_pencil_cost / profit_per_pop

    # FA
    answer = num_pops_to_sell
    return answer