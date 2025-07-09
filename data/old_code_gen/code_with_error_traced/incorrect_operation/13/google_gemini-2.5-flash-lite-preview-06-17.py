def solve(
    cheddar_cost: int = 10, # Jasper buys 2 pounds of cheddar cheese for $10
    cheddar_pounds: int = 2, # Jasper buys 2 pounds of cheddar cheese
    cream_cheese_pounds: int = 1 # a pound of cream cheese
):
    """Index: 13.
    Returns: the total amount Jasper spent on the ingredients.
    """

    #: L1
    cream_cheese_cost = cheddar_cost / 2 # eval: 5.0 = 10 / 2

    #: L2
    cold_cuts_cost = cheddar_cost * 2 # eval: 20 = 10 * 2

    #: L3
    total_cost = cheddar_cost - cream_cheese_cost + cold_cuts_cost # eval: 25.0 = 10 - 5.0 + 20

    #: FA
    answer = total_cost
    return answer # eval: return 25.0
