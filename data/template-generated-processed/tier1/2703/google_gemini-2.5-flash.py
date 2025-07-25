def solve():
    """Index: 2703.
    Returns: the total number of crayons.
    """
    # L1
    num_boxes_orange = 6 # 6 boxes of crayons
    orange_crayons_per_box = 8 # 8 orange crayons
    total_orange_crayons = num_boxes_orange * orange_crayons_per_box

    # L2
    num_boxes_blue = 7 # 7 boxes of crayons
    blue_crayons_per_box = 5 # 5 blue crayons
    total_blue_crayons = num_boxes_blue * blue_crayons_per_box

    # L4
    total_red_crayons = 11 # 1 box of 11 red crayons
    total_crayons = total_orange_crayons + total_blue_crayons + total_red_crayons

    # FA
    answer = total_crayons
    return answer