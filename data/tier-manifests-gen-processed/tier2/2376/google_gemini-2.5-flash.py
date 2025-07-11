def solve():
    """Index: 2376.
    Returns: the total cost of Juanita's dessert.
    """
    # L1
    num_scoops_ice_cream = 2 # 2 scoops of ice cream
    cost_per_scoop_ice_cream = 1.00 # $1.00 per scoop
    ice_cream_cost = num_scoops_ice_cream * cost_per_scoop_ice_cream

    # L2
    syrup_multiplier = 2 # double syrup
    cost_per_syrup = 0.50 # $0.50
    syrup_cost = syrup_multiplier * cost_per_syrup

    # L3
    brownie_cost = 2.50 # The brownie cost $2.50
    nuts_cost = 1.50 # nuts cost $1.50
    total_cost = brownie_cost + ice_cream_cost + syrup_cost + nuts_cost

    # FA
    answer = total_cost
    return answer