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
    beef_cost = beef_price_per_pound * beef_pounds

    #: L2
    chicken_pounds = beef_pounds * chicken_multiplier

    #: L3

    #: L4
    total_cost = beef_cost + chicken_multiplier

    #: FA
    answer = total_cost
    return answer