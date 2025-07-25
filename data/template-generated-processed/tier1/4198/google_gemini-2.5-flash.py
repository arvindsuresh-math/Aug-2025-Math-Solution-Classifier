def solve():
    """Index: 4198.
    Returns: the total number of balloons.
    """
    # L1
    num_boxes = 5 # 5 boxes of balloons
    bags_per_box = 8 # 8 bags of balloons
    total_bags = num_boxes * bags_per_box

    # L2
    balloons_per_bag = 12 # 12 balloons in each bag
    total_balloons = total_bags * balloons_per_bag

    # FA
    answer = total_balloons
    return answer