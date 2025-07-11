def solve(
    cheddar_cost: int = 10,  # 2 pounds of cheddar cheese for $10
    cheddar_pounds: int = 2,  # 2 pounds of cheddar cheese
    cream_cheese_cost: float = 0,  # a pound of cream cheese that cost half the price of the cheddar cheese
    cold_cuts_cost: float = 0  # a pack of cold cuts that cost twice the price of the cheddar cheese
):
    """Index: 13.
    Returns: the total amount Jasper spends on the ingredients.
    """
    #: L1
    cream_cheese_cost = cheddar_cost / 2

    #: L2
    cold_cuts_cost = cheddar_cost * 2

    #: L3
    total_spent = cheddar_cost + cream_cheese_cost + cold_cuts_cost

    answer = total_spent  # FINAL ANSWER
    return answer