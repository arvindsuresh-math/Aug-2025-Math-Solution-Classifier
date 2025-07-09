def solve(
    beef_pounds: int = 1000,  # John orders 1000 pounds of beef
    beef_price_per_pound: int = 8,  # at $8 per pound
    chicken_multiplier: int = 2,  # he orders twice that much chicken
    chicken_price_per_pound: int = 3  # at $3 per pound
):
    """Index: 93.
    Returns: the total cost of beef and chicken ordered.
    """

    #: L1
    beef_cost = beef_pounds * beef_price_per_pound # eval: 8000 = 1000 * 8

    #: L2
    chicken_pounds = beef_pounds * beef_price_per_pound # eval: 8000 = 1000 * 8

    #: L3
    chicken_cost = chicken_pounds * chicken_price_per_pound # eval: 24000 = 8000 * 3

    #: L4
    total_cost = beef_cost + chicken_cost # eval: 32000 = 8000 + 24000

    #: FA
    answer = total_cost
    return answer # eval: return 32000
