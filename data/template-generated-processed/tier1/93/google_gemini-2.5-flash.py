def solve():
    """Index: 93.
    Returns: the total cost of the food order.
    """
    # L1
    beef_price_per_pound = 8 # $8 per pound
    beef_pounds = 1000 # 1000 pounds of beef
    beef_cost = beef_price_per_pound * beef_pounds

    # L2
    chicken_multiplier = 2 # twice that much chicken
    chicken_pounds = beef_pounds * chicken_multiplier

    # L3
    chicken_price_per_pound = 3 # $3 per pound
    chicken_cost = chicken_pounds * chicken_price_per_pound

    # L4
    total_cost = beef_cost + chicken_cost

    # FA
    answer = total_cost
    return answer