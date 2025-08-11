def solve():
    """Index: 1624.
    Returns: the total cost of 3 kg of chicken and 1 kg of pork.
    """
    # L1
    pork_per_kg = 6 # kilogram of pork costs $6
    chicken_less_than_pork = 2 # kilogram of chicken costs $2 less
    chicken_per_kg = pork_per_kg - chicken_less_than_pork

    # L2
    chicken_kg = 3 # 3-kilogram of chicken
    chicken_total = chicken_per_kg * chicken_kg

    # L3
    pork_kg = 1 # a kilogram of pork
    pork_total = pork_per_kg * pork_kg
    total_cost = chicken_total + pork_total

    # FA
    answer = total_cost
    return answer