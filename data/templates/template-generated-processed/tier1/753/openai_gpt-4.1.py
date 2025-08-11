def solve():
    """Index: 753.
    Returns: the total kilograms of potatoes sold in the whole day.
    """
    # L1
    morning_bags = 29 # 29 bags of potatoes in the morning
    afternoon_bags = 17 # 17 bags of potatoes in the afternoon
    total_bags = morning_bags + afternoon_bags

    # L2
    bag_weight_kg = 7 # each bag of potatoes weighs 7kg
    total_kg = total_bags * bag_weight_kg

    # FA
    answer = total_kg
    return answer