def solve():
    """Index: 7088.
    Returns: the total cost of a sundae with toppings.
    """
    # L1
    num_toppings = 10 # 10 toppings
    cost_per_topping = 0.50 # $0.50 per topping
    total_topping_cost = num_toppings * cost_per_topping

    # L2
    ice_cream_cost = 2.00 # Ice cream costs $2.00
    total_sundae_cost = total_topping_cost + ice_cream_cost

    # FA
    answer = total_sundae_cost
    return answer