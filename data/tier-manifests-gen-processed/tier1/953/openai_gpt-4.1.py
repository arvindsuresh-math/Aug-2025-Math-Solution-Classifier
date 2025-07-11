def solve():
    """Index: 953.
    Returns: the number of chickens Wendi has at the end.
    """
    # L1
    initial_chickens = 4 # Wendi brought home 4 chickens
    multiplier_for_double = 2 # double the number of chickens
    after_doubling = initial_chickens * multiplier_for_double

    # L2
    chickens_eaten = 1 # a neighbor's dog ate one of her chickens
    after_dog = after_doubling - chickens_eaten

    # L3
    ten = 10 # WK
    four = 4 # WK
    four_less_than_ten = ten - four

    # L4
    total_chickens = after_dog + four_less_than_ten

    # FA
    answer = total_chickens
    return answer