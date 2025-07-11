def solve():
    """Index: 1683.
    Returns: the total number of highlighters in Carrie's desk drawer.
    """
    # L1
    yellow_highlighters = 7 # 7 yellow highlighters
    pink_more_than_yellow = 7 # 7 more pink highlighters than yellow highlighters
    pink_highlighters = yellow_highlighters + pink_more_than_yellow

    # L2
    blue_more_than_pink = 5 # 5 more blue highlighters than pink highlighters
    blue_highlighters = pink_highlighters + blue_more_than_pink

    # L4
    total_highlighters = yellow_highlighters + pink_highlighters + blue_highlighters

    # FA
    answer = total_highlighters
    return answer