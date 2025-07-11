def solve():
    """Index: 920.
    Returns: the total amount Betty spends on drinks, cakes, and ice creams.
    """
    # L1
    unit_cost_drink = 2 # unit cost of $2 (drinks)
    num_drinks = 10 # buys 10 drinks
    drinks_total = unit_cost_drink * num_drinks

    # L2
    unit_cost_cake = 10 # unit cost of $10 (cakes)
    num_cakes = 5 # buys 5 cakes
    cakes_total = unit_cost_cake * num_cakes

    # L3
    unit_cost_ice_cream = 5 # unit cost of $5 (ice creams)
    num_ice_creams = 100 # buys 100 ice creams
    ice_creams_total = unit_cost_ice_cream * num_ice_creams

    # L4
    total_spent = drinks_total + cakes_total + ice_creams_total

    # FA
    answer = total_spent
    return answer