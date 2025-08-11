def solve():
    """Index: 2578.
    Returns: the total number of rubber bands Harper and his brother have together.
    """
    # L1
    harper_bands = 15 # Harper has 15 rubber bands
    brother_fewer = 6 # His brother has 6 fewer rubber bands than he has
    brother_bands = harper_bands - brother_fewer

    # L2
    total_bands = harper_bands + brother_bands

    # FA
    answer = total_bands
    return answer