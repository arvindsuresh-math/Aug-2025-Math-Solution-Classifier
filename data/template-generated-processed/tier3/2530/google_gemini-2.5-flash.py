def solve():
    """Index: 2530.
    Returns: the total cost of coffee.
    """
    # L1
    num_dozens = 3 # 3 dozen donuts
    donuts_per_dozen = 12 # WK
    total_donuts = num_dozens * donuts_per_dozen

    # L2
    ounces_per_donut = 2 # for each donut they need 2 ounces of coffee
    total_ounces_needed = ounces_per_donut * total_donuts

    # L3
    ounces_per_pot = 12 # Every pot of coffee she makes contains 12 ounces
    num_pots = total_ounces_needed / ounces_per_pot

    # L4
    cost_per_pot = 3 # costs $3 to make
    total_cost = num_pots * cost_per_pot

    # FA
    answer = total_cost
    return answer