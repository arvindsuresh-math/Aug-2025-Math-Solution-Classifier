def solve():
    """Index: 2857.
    Returns: the total number of T-shirts Dave bought.
    """
    # L1
    num_white_packs = 3 # 3 packs of white T-shirts
    white_pack_size = 6 # packs of 6
    num_white_shirts = num_white_packs * white_pack_size

    # L2
    num_blue_packs = 2 # 2 packs of blue T-shirts
    blue_pack_size = 4 # packs of 4
    num_blue_shirts = num_blue_packs * blue_pack_size

    # L3
    total_shirts = num_white_shirts + num_blue_shirts

    # FA
    answer = total_shirts
    return answer