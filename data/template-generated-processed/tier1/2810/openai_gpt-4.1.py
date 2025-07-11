def solve():
    """Index: 2810.
    Returns: the total number of crayons in the box.
    """
    # L1
    red_to_blue_ratio = 4 # four times as many red crayons as blue crayons
    blue_crayons = 3 # there are 3 blue crayons
    red_crayons = red_to_blue_ratio * blue_crayons

    # L2
    total_crayons = red_crayons + blue_crayons

    # FA
    answer = total_crayons
    return answer