def solve():
    """Index: 1624.
    Returns: the total cost of chicken and pork.
    """
    # L1
    pork_cost_per_kg = 6 # A kilogram of pork costs $6
    chicken_cost_less_than_pork = 2 # chicken costs $2 less
    chicken_cost_per_kg = pork_cost_per_kg - chicken_cost_less_than_pork

    # L2
    chicken_quantity_bought = 3 # a 3-kilogram of chicken
    cost_of_3kg_chicken = chicken_cost_per_kg * chicken_quantity_bought

    # L3
    total_cost = cost_of_3kg_chicken + pork_cost_per_kg

    # FA
    answer = total_cost
    return answer