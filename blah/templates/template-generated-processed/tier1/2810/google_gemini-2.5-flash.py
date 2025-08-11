def solve():
    """Index: 2810.
    Returns: the total number of crayons in the box.
    """
    # L1
    four_times = 4 # four times as many red crayons
    num_blue_crayons = 3 # 3 blue crayons
    num_red_crayons = four_times * num_blue_crayons

    # L2
    total_crayons = num_red_crayons + num_blue_crayons

    # FA
    answer = total_crayons
    return answer