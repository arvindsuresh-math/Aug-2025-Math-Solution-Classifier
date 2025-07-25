def solve():
    """Index: 4286.
    Returns: the number of black-haired girls present in the choir.
    """
    # L1
    initial_total_girls = 80 # 80 blonde and black-haired girls
    added_girls = 10 # add 10 more girls
    total_girls_after_addition = initial_total_girls + added_girls

    # L2
    initial_blonde_girls = 30 # 30 blonde-haired girls in the choir initially
    total_blonde_girls = initial_blonde_girls + added_girls

    # L3
    black_haired_girls = total_girls_after_addition - total_blonde_girls

    # FA
    answer = black_haired_girls
    return answer