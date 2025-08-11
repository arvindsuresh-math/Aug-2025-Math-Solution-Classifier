def solve():
    """Index: 2376.
    Returns: the total cost of Juanita's dessert order.
    """
    # L1
    num_scoops = 2 # 2 scoops of ice cream
    ice_cream_cost_per_scoop = 1.00 # $1.00 per scoop
    ice_cream_total = num_scoops * ice_cream_cost_per_scoop

    # L2
    num_syrups = 2 # double syrup
    syrup_cost_per = 0.50 # $0.50 per syrup
    syrup_total = num_syrups * syrup_cost_per

    # L3
    brownie_cost = 2.5 # The brownie is $2.50
    nuts_cost = 1.5 # nuts cost $1.50
    total_cost = brownie_cost + ice_cream_total + syrup_total + nuts_cost

    # FA
    answer = total_cost
    return answer