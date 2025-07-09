def solve(
    beef_pounds: int = 1000, # 1000 pounds of beef
    beef_price_per_pound: int = 8, # for $8 per pound
    chicken_multiplier: int = 2, # twice that much chicken
    chicken_price_per_pound: int = 3 # at $3 per pound
):
    """Index: 93.
    Returns: the total cost of the beef and chicken.
    """

    #: L1
    beef_cost = beef_price_per_pound * beef_pounds # eval: 8000 = 8 * 1000

    #: L2
    chicken_pounds = beef_pounds * chicken_multiplier # eval: 2000 = 1000 * 2

    #: L3
    chicken_cost = chicken_pounds * chicken_price_per_pound # eval: 6000 = 2000 * 3

    #: L4
    total_cost = chicken_pounds + chicken_cost # eval: 8000 = 2000 + 6000

    #: FA
    answer = total_cost
    return answer # eval: return 8000
