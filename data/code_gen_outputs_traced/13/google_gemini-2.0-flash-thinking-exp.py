def solve(
    cheddar_pounds: int = 2, # buys 2 pounds of cheddar cheese
    cheddar_cost: int = 10, # for $10
    cream_cheese_cost_factor: float = 1/2, # cream cheese that cost half the price of the cheddar cheese
    cold_cuts_cost_factor: int = 2 # pack of cold cuts that cost twice the price of the cheddar cheese
):
    """Index: 13.
    Returns: the total cost of the ingredients.
    """

    #: L1
    cream_cheese_cost = cheddar_cost * cream_cheese_cost_factor # eval: 5.0 = 10 * 0.5

    #: L2
    cold_cuts_cost = cheddar_cost * cold_cuts_cost_factor # eval: 20 = 10 * 2

    #: L3
    total_cost = cheddar_cost + cream_cheese_cost + cold_cuts_cost # eval: 35.0 = 10 + 5.0 + 20

    #: FA
    answer = total_cost
    return answer # eval: return 35.0
