def solve():
    """Index: 2216.
    Returns: the number of 400-ml bottles of dye Jenna needs to buy.
    """
    # L1
    dots_per_blouse = 20 # Each blouse gets 20 dots
    ml_per_dot = 10 # each dot takes 10 ml of black dye
    dye_per_blouse = dots_per_blouse * ml_per_dot

    # L2
    num_blouses = 100 # to dye 100 blouses
    total_dye_needed = dye_per_blouse * num_blouses

    # L3
    bottle_capacity = 400 # 400-ml bottles of dye
    bottles_needed = total_dye_needed / bottle_capacity

    # FA
    answer = bottles_needed
    return answer