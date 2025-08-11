def solve():
    """Index: 5645.
    Returns: the weight of 8 bags of oranges.
    """
    # L1
    total_weight_12_bags = 24 # 24 pounds
    num_bags_12 = 12 # 12 bags of oranges
    weight_per_bag = total_weight_12_bags / num_bags_12

    # L2
    num_bags_8 = 8 # 8 bags
    weight_8_bags = num_bags_8 * weight_per_bag

    # FA
    answer = weight_8_bags
    return answer