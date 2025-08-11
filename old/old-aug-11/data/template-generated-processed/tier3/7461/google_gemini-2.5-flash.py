def solve():
    """Index: 7461.
    Returns: the total population of bears in the park.
    """
    # L1
    black_bears = 60 # number of black bears in the park is 60
    more_brown_bears = 40 # 40 more brown bears than black bears
    brown_bears = black_bears + more_brown_bears

    # L2
    black_and_brown_bears = brown_bears + black_bears

    # L3
    white_bears_divisor = 2 # twice as many black bears as white bears
    white_bears = black_bears / white_bears_divisor

    # L4
    total_bears = white_bears + black_and_brown_bears

    # FA
    answer = total_bears
    return answer