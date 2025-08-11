def solve():
    """Index: 3019.
    Returns: the final number of marbles Janelle has.
    """
    # L1
    num_bags_blue = 6 # 6 bags of blue marbles
    marbles_per_bag = 10 # 10 marbles in each bag
    total_blue_marbles = num_bags_blue * marbles_per_bag

    # L2
    initial_green_marbles = 26 # 26 green marbles
    total_marbles_before_gift = initial_green_marbles + total_blue_marbles

    # L3
    gift_green_marbles = 6 # 6 green marbles
    gift_blue_marbles = 8 # 8 blue marbles
    total_gift_marbles = gift_green_marbles + gift_blue_marbles

    # L4
    final_marbles = total_marbles_before_gift - total_gift_marbles

    # FA
    answer = final_marbles
    return answer