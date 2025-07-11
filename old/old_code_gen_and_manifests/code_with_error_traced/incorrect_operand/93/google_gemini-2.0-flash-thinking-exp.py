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
    chicken_pounds = beef_pounds * beef_pounds # eval: 1000000 = 1000 * 1000

    #: L3
    chicken_cost = chicken_pounds * chicken_price_per_pound # eval: 3000000 = 1000000 * 3

    #: L4
    total_cost = beef_cost + chicken_cost # eval: 3008000 = 8000 + 3000000

    #: FA
    answer = total_cost
    return answer # eval: return 3008000
