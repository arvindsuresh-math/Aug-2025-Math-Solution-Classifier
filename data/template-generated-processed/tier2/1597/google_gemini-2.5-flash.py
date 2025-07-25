def solve():
    """Index: 1597.
    Returns: the total number of plumeria flowers Jaynie must pick.
    """
    # L1
    plumeria_per_lei_dozen = 2.5 # 2 and half dozen plumeria flowers
    flowers_per_dozen = 12 # WK
    flowers_per_lei = plumeria_per_lei_dozen * flowers_per_dozen

    # L2
    num_leis = 4 # 4 leis
    total_flowers = flowers_per_lei * num_leis

    # FA
    answer = total_flowers
    return answer