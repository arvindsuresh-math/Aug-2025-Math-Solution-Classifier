def solve():
    """Index: 2703.
    Returns: the total number of crayons.
    """
    # L1
    orange_boxes = 6 # 6 boxes of crayons that hold 8 orange crayons
    orange_per_box = 8 # 8 orange crayons per box
    orange_total = orange_boxes * orange_per_box

    # L2
    blue_boxes = 7 # 7 boxes of crayons that have 5 blue crayons
    blue_per_box = 5 # 5 blue crayons per box
    blue_total = blue_boxes * blue_per_box

    # L3
    red_total = 11 # 1 box of 11 red crayons

    # L4
    total_crayons = orange_total + blue_total + red_total

    # FA
    answer = total_crayons
    return answer