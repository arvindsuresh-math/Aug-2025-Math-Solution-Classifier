def solve():
    """Index: 753.
    Returns: the total kilograms of potatoes sold for the whole day.
    """
    # L1
    morning_bags = 29 # 29 bags of potatoes in the morning
    afternoon_bags = 17 # 17 bags of potatoes
    total_bags = morning_bags + afternoon_bags

    # L2
    weight_per_bag = 7 # each bag of potatoes weighs 7kg
    total_weight_kg = total_bags * weight_per_bag

    # FA
    answer = total_weight_kg
    return answer