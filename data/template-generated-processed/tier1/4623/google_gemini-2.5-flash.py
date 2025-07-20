def solve():
    """Index: 4623.
    Returns: the number of shirts Steven has.
    """
    # L1
    andrew_multiplier = 6 # 6 times as many shirts as Brian
    brian_shirts = 3 # Brian has 3 shirts
    andrew_shirts = andrew_multiplier * brian_shirts

    # L2
    steven_multiplier = 4 # 4 times as many shirts as Andrew
    steven_shirts = steven_multiplier * andrew_shirts

    # FA
    answer = steven_shirts
    return answer