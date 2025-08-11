def solve():
    """Index: 1730.
    Returns: the amount saved by buying 3 sets of 2 dozens instead of 6 sets of 1 dozen.
    """
    # L1
    price_per_dozen = 8 # it costs $8 for a dozen
    sets_of_one_dozen = 6 # 6 sets of 1 dozen
    cost_one_dozen_sets = price_per_dozen * sets_of_one_dozen

    # L2
    price_per_two_dozen = 14 # it costs $14 for 2 dozens
    sets_of_two_dozen = 3 # 3 sets of 2 dozens
    cost_two_dozen_sets = price_per_two_dozen * sets_of_two_dozen

    # L3
    savings = cost_one_dozen_sets - cost_two_dozen_sets

    # FA
    answer = savings
    return answer