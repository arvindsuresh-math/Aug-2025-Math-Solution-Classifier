def solve():
    """Index: 147.
    Returns: the number of crayons Mary has left.
    """
    # L1
    green_crayons_initial = 5 # 5 green crayons
    blue_crayons_initial = 8 # 8 blue crayons
    total_crayons_initial = green_crayons_initial + blue_crayons_initial

    # L2
    green_crayons_given = 3 # 3 green crayons
    blue_crayons_given = 1 # 1 blue crayon
    total_crayons_given = green_crayons_given + blue_crayons_given

    # L3
    crayons_left = total_crayons_initial - total_crayons_given

    # FA
    answer = crayons_left
    return answer