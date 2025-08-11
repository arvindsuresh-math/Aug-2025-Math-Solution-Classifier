def solve():
    """Index: 4081.
    Returns: the total number of shirts Mandy bought.
    """
    # L1
    packs_black_shirts = 3 # 3 packs of black shirts
    shirts_per_pack_black = 5 # packs of 5
    num_black_shirts = packs_black_shirts * shirts_per_pack_black

    # L2
    packs_yellow_shirts = 3 # 3 packs of yellow shirts
    shirts_per_pack_yellow = 2 # packs of 2
    num_yellow_shirts = packs_yellow_shirts * shirts_per_pack_yellow

    # L3
    total_shirts = num_black_shirts + num_yellow_shirts

    # FA
    answer = total_shirts
    return answer