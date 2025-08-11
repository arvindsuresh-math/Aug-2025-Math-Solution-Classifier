def solve():
    """Index: 1355.
    Returns: the total number of pieces of clothes Mr. Jones owns.
    """
    # L1
    shirts_per_pant = 6 # 6 shirts for every pair of pants
    num_pants = 40 # he has 40 pants
    num_shirts = shirts_per_pant * num_pants

    # L2
    total_clothes = num_shirts + num_pants

    # FA
    answer = total_clothes
    return answer