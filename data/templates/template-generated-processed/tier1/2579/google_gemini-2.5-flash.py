def solve():
    """Index: 2579.
    Returns: the difference in crayons given to Lea and Mae.
    """
    # L1
    crayons_per_box = 8 # 8 crayons in each box
    num_boxes = 4 # 4 boxes of crayons
    initial_crayons = crayons_per_box * num_boxes

    # L2
    crayons_given_to_mae = 5 # gave 5 crayons to Mae
    crayons_after_mae = initial_crayons - crayons_given_to_mae

    # L3
    crayons_left = 15 # has only 15 crayons left
    crayons_given_to_lea = crayons_after_mae - crayons_left

    # L4
    difference_lea_mae = crayons_given_to_lea - crayons_given_to_mae

    # FA
    answer = difference_lea_mae
    return answer