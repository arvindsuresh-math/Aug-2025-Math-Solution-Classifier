def solve(
    cheddar_cheese_pounds: int = 2,  # Jasper buys 2 pounds of cheddar cheese
    cheddar_cheese_price: int = 10,  # for $10
    cream_cheese_price_fraction: float = 0.5,  # cream cheese that cost half the price of the cheddar cheese
    cold_cuts_price_multiplier: int = 2  # a pack of cold cuts that cost twice the price of the cheddar cheese
):
    """Index: 13.
    Returns: the total amount Jasper spends on charcuterie ingredients.
    """
    #: L1
    cream_cheese_price = cheddar_cheese_price * cream_cheese_price_fraction

    #: L2
    cold_cuts_price = cheddar_cheese_price * cold_cuts_price_multiplier

    #: L3
    total_ingredients_cost = cheddar_cheese_price + cream_cheese_price + cold_cuts_price

    answer = total_ingredients_cost  # FINAL ANSWER
    return answer