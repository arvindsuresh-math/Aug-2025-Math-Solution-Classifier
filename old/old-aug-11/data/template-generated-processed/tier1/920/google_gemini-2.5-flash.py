def solve():
    """Index: 920.
    Returns: the total amount Betty spends on drinks, cakes, and ice creams.
    """
    # L1
    drink_unit_cost = 2 # unit cost of $2
    num_drinks = 10 # 10 drinks
    cost_drinks = drink_unit_cost * num_drinks

    # L2
    cake_unit_cost = 10 # unit cost of $10
    num_cakes = 5 # 5 cakes
    cost_cakes = cake_unit_cost * num_cakes

    # L3
    ice_cream_unit_cost = 5 # unit cost of $5
    num_ice_creams = 100 # 100 ice creams
    cost_ice_creams = ice_cream_unit_cost * num_ice_creams

    # L4
    total_cost = cost_drinks + cost_cakes + cost_ice_creams

    # FA
    answer = total_cost
    return answer