def solve():
    """Index: 147.
    Returns: the number of crayons Mary has left after giving some to Becky.
    """
    # L1
    green_crayons = 5 # 5 green crayons
    blue_crayons = 8 # 8 blue crayons
    total_crayons = green_crayons + blue_crayons

    # L2
    green_given = 3 # gives out 3 green crayons
    blue_given = 1 # gives out 1 blue crayon
    total_given = green_given + blue_given

    # L3
    crayons_left = total_crayons - total_given

    # FA
    answer = crayons_left
    return answer