def solve(
    beef_pounds: int = 1000, # orders 1000 pounds of beef
    beef_price_per_pound: int = 8, # for $8 per pound
    chicken_quantity_multiplier: int = 2, # orders twice that much chicken
    chicken_price_per_pound: int = 3 # at $3 per pound
):
    """Index: 93.
    Returns: the total cost of the food order.
    """

    #: L1
    beef_cost = beef_price_per_pound * beef_pounds # eval: 8000 = 8 * 1000

    #: L2
    chicken_pounds = beef_pounds * chicken_quantity_multiplier # eval: 2000 = 1000 * 2

    #: L3
    chicken_cost = 6010 # eval: 6010 = 6010

    #: L4
    total_cost = beef_cost + chicken_cost # eval: 14010 = 8000 + 6010

    #: FA
    answer = total_cost
    return answer # eval: return 14010
