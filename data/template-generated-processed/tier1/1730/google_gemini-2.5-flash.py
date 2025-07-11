def solve():
    """Index: 1730.
    Returns: the amount saved from buying 3 sets of 2 dozens than buying 6 sets of 1 dozen.
    """
    # L1
    cost_one_dozen = 8 # it costs $8
    num_sets_one_dozen = 6 # 6 sets of 1 dozen
    cost_six_sets_one_dozen = cost_one_dozen * num_sets_one_dozen

    # L2
    cost_two_dozens = 14 # it costs $14
    num_sets_two_dozens = 3 # 3 sets of 2 dozens
    cost_three_sets_two_dozens = cost_two_dozens * num_sets_two_dozens

    # L3
    savings = cost_six_sets_one_dozen - cost_three_sets_two_dozens

    # FA
    answer = savings
    return answer