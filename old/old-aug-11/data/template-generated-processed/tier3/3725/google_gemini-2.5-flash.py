def solve():
    """Index: 3725.
    Returns: the number of pounds purchased over the minimum.
    """
    # L1
    total_spent = 105 # spent $105 on peanuts
    cost_per_pound = 3 # $3 per pound
    pounds_bought = total_spent / cost_per_pound

    # L2
    minimum_pounds = 15 # 15-pound minimum
    pounds_over_minimum = pounds_bought - minimum_pounds

    # FA
    answer = pounds_over_minimum
    return answer