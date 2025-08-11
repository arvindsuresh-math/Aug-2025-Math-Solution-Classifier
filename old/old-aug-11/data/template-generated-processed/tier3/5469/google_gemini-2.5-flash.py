def solve():
    """Index: 5469.
    Returns: the average number of brown M&M's in a bag.
    """
    # L1
    first_bag_brown_mms = 9 # 9 brown M&M's
    second_bag_brown_mms = 12 # 12
    third_fourth_bag_brown_mms = 8 # 8 brown M&M's
    fifth_bag_brown_mms = 3 # 3 brown M&M's
    total_brown_mms = first_bag_brown_mms + second_bag_brown_mms + third_fourth_bag_brown_mms + third_fourth_bag_brown_mms + fifth_bag_brown_mms

    # L2
    num_bags = 5 # Out of 5 bags
    average_brown_mms_per_bag = total_brown_mms / num_bags

    # FA
    answer = average_brown_mms_per_bag
    return answer