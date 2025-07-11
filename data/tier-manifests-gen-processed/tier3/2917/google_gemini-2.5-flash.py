def solve():
    """Index: 2917.
    Returns: the number of toys in the larger pile.
    """
    # L1
    total_toys = 120 # two piles of toys added together make 120 toys in total
    ratio_sum = 3 # WK
    smaller_pile = total_toys / ratio_sum

    # L2
    multiplier = 2 # the larger of the two piles is twice as big as the smaller one
    larger_pile = smaller_pile * multiplier

    # FA
    answer = larger_pile
    return answer