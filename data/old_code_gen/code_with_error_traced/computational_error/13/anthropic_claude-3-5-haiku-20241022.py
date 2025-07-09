def solve(
    cheddar_cheese_weight: int = 2,  # 2 pounds of cheddar cheese
    cheddar_cheese_price: int = 10,  # for $10
    cream_cheese_weight: int = 1,  # a pound of cream cheese
    cold_cuts_multiplier: int = 2  # cold cuts cost twice the price of cheddar cheese
):
    """Index: 13.
    Returns: the total amount Jasper spends on charcuterie ingredients."""

    #: L1
    cream_cheese_price = 4.0 # eval: 4.0 = 4.0

    #: L2
    cold_cuts_price = cheddar_cheese_price * cold_cuts_multiplier # eval: 20 = 10 * 2

    #: L3
    total_spent = cheddar_cheese_price + cream_cheese_price + cold_cuts_price # eval: 34.0 = 10 + 4.0 + 20

    #: FA
    answer = total_spent
    return answer # eval: return 34.0
