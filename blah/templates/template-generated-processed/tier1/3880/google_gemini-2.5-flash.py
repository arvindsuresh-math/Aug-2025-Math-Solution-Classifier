def solve():
    """Index: 3880.
    Returns: how much more money Farmer Brown will need to meet his new requirements.
    """
    # L1
    previous_cost_per_bale = 15 # $15 per bale
    initial_bales = 10 # ten bales of hay
    previous_total_cost = previous_cost_per_bale * initial_bales

    # L2
    double_factor = 2 # double the delivery
    new_bales_quantity = initial_bales * double_factor

    # L3
    new_cost_per_bale = 18 # $18 per bale
    new_total_cost = new_cost_per_bale * new_bales_quantity

    # L4
    additional_money_needed = new_total_cost - previous_total_cost

    # FA
    answer = additional_money_needed
    return answer