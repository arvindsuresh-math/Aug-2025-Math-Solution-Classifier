def solve():
    """Index: 5595.
    Returns: the cost of a ticket to Mars when Matty is 30.
    """
    # L1
    matty_age = 30 # when Matty is 30
    halving_interval = 10 # every 10 years
    num_halvings = matty_age / halving_interval

    # L2
    initial_cost = 1000000 # $1,000,000
    halving_factor = 2 # halved
    cost_after_first_halving = initial_cost / halving_factor

    # L3
    cost_after_second_halving = cost_after_first_halving / halving_factor

    # L4
    cost_after_third_halving = cost_after_second_halving / halving_factor

    # FA
    answer = cost_after_third_halving
    return answer