def solve():
    """Index: 13.
    Returns: the total amount Jasper spends on the ingredients.
    """
    # L1
    cheddar_price = 10 # $10 for cheddar cheese
    cream_cheese_divisor = 2 # cost half the price of the cheddar cheese
    cream_cheese_price = cheddar_price / cream_cheese_divisor

    # L2
    cold_cuts_multiplier = 2 # cost twice the price of the cheddar cheese
    cold_cuts_price = cheddar_price * cold_cuts_multiplier

    # L3
    total_spent = cheddar_price + cream_cheese_price + cold_cuts_price

    # FA
    answer = total_spent
    return answer