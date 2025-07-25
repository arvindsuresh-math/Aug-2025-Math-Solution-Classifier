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
    beef_cost = beef_pounds * beef_price_per_pound

    #: L2
    chicken_pounds = beef_pounds * chicken_multiplier

    #: L3
    chicken_cost = chicken_pounds * chicken_price_per_pound

    #: L4
    total_cost = beef_cost + chicken_cost

    answer = total_cost  # FINAL ANSWER
    return answer