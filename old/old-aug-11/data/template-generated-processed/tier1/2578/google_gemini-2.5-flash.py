def solve():
    """Index: 2578.
    Returns: the total number of rubber bands Harper and his brother have together.
    """
    # L1
    harper_rubber_bands = 15 # Harper has 15 rubber bands
    fewer_than_harper = 6 # 6 fewer rubber bands than he has
    brother_rubber_bands = harper_rubber_bands - fewer_than_harper

    # L2
    total_rubber_bands = harper_rubber_bands + brother_rubber_bands

    # FA
    answer = total_rubber_bands
    return answer