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

    #: L4
    total_cost = beef_cost + chicken_multiplier # eval: 8002 = 8000 + 2

    #: FA
    answer = total_cost
    return answer # eval: return 8002
