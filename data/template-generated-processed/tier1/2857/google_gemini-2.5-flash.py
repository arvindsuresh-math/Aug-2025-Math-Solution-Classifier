def solve():
    """Index: 2857.
    Returns: the total number of T-shirts Dave bought.
    """
    # L1
    packs_white_shirts = 3 # 3 packs of white T-shirts
    white_shirts_per_pack = 6 # white T-shirts come in packs of 6
    total_white_shirts = packs_white_shirts * white_shirts_per_pack

    # L2
    packs_blue_shirts = 2 # 2 packs of blue T-shirts
    blue_shirts_per_pack = 4 # blue T-shirts come in packs of 4
    total_blue_shirts = packs_blue_shirts * blue_shirts_per_pack

    # L3
    total_shirts_bought = total_white_shirts + total_blue_shirts

    # FA
    answer = total_shirts_bought
    return answer