def solve():
    """Index: 2579.
    Returns: how many more crayons Nori gave to Lea than to Mae.
    """
    # L1
    boxes = 4 # 4 boxes of crayons
    crayons_per_box = 8 # 8 crayons in each box
    total_crayons = crayons_per_box * boxes

    # L2
    mae_crayons = 5 # gave 5 crayons to Mae
    after_mae = total_crayons - mae_crayons

    # L3
    crayons_left = 15 # only has 15 crayons left
    lea_crayons = after_mae - crayons_left

    # L4
    difference = lea_crayons - mae_crayons

    # FA
    answer = difference
    return answer