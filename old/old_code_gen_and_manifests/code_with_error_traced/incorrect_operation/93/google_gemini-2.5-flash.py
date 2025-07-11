def solve(
        beef_pounds: int = 1000, # 1000 pounds of beef
        beef_price_per_pound: int = 8, # $8 per pound
        chicken_quantity_multiplier: int = 2, # twice that much chicken
        chicken_price_per_pound: int = 3 # $3 per pound
    ):
    """Index: 93.
    Returns: the total cost of all food ordered.
    """

    #: L1
    cost_beef = beef_price_per_pound - beef_pounds # eval: -992 = 8 - 1000

    #: L2
    chicken_pounds = beef_pounds * chicken_quantity_multiplier # eval: 2000 = 1000 * 2

    #: L3
    cost_chicken = chicken_pounds * chicken_price_per_pound # eval: 6000 = 2000 * 3

    #: L4
    total_cost = cost_beef + cost_chicken # eval: 5008 = -992 + 6000

    #: FA
    answer = total_cost
    return answer # eval: return 5008
