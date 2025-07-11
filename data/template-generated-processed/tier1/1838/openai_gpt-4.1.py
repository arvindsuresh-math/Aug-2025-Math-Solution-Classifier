def solve():
    """Index: 1838.
    Returns: the total number of blocks Jacob has in all.
    """
    # L1
    red_blocks = 18 # 18 red blocks
    yellow_more_than_red = 7 # 7 more yellow blocks than red blocks
    yellow_blocks = red_blocks + yellow_more_than_red

    # L2
    blue_more_than_red = 14 # 14 more blue blocks than red blocks
    blue_blocks = red_blocks + blue_more_than_red

    # L3
    total_blocks = red_blocks + yellow_blocks + blue_blocks

    # FA
    answer = total_blocks
    return answer