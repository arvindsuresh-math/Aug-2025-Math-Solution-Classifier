def solve(
        pounds_cheddar: int = 2, # 2 pounds of cheddar cheese
        cost_cheddar_total: int = 10, # $10 (for 2 pounds of cheddar cheese)
        cream_cheese_price_divisor: int = 2, # half the price of the cheddar cheese
        cold_cuts_price_multiplier: int = 2 # twice the price of the cheddar cheese
    ):
    """Index: 13.
    Returns: the total amount spent on ingredients.
    """

    #: L1
    cost_cream_cheese = cost_cheddar_total / cream_cheese_price_divisor # eval: 5.0 = 10 / 2

    #: L2
    cost_cold_cuts = cost_cheddar_total * cold_cuts_price_multiplier # eval: 20 = 10 * 2

    #: L3
    total_spent = cost_cheddar_total + cost_cream_cheese + cost_cold_cuts # eval: 35.0 = 10 + 5.0 + 20

    #: FA
    answer = total_spent
    return answer # eval: return 35.0
