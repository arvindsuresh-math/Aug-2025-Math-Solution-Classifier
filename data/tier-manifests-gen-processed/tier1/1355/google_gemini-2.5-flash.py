def solve():
    """Index: 1355.
    Returns: the total number of pieces of clothes Mr. Jones owns.
    """
    # L1
    shirts_per_pant_pair = 6 # 6 shirts for every pair of pants
    num_pants = 40 # he has 40 pants
    total_shirts = shirts_per_pant_pair * num_pants

    # L2
    total_clothes = total_shirts + num_pants

    # FA
    answer = total_clothes
    return answer