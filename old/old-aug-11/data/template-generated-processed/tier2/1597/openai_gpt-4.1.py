def solve():
    """Index: 1597.
    Returns: the number of plumeria flowers Jaynie must pick to make 4 leis.
    """
    # L1
    flowers_per_dozen = 12 # dozen
    dozens_per_lei = 2.5 # 2 and half dozen plumeria flowers to make 1 lei
    flowers_per_lei = flowers_per_dozen * dozens_per_lei

    # L2
    num_leis = 4 # she wants to make 4 leis
    total_flowers = flowers_per_lei * num_leis

    # FA
    answer = total_flowers
    return answer