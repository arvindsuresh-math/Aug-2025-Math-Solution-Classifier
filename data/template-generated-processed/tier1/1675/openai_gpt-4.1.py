def solve():
    """Index: 1675.
    Returns: the total weight of the lorry after being loaded with apples.
    """
    # L1
    num_bags = 20 # 20 bags of apples
    weight_per_bag = 60 # each weighing 60 pounds
    total_apples_weight = num_bags * weight_per_bag

    # L2
    lorry_empty_weight = 500 # lorry is 500 pounds when empty
    total_weight = lorry_empty_weight + total_apples_weight

    # FA
    answer = total_weight
    return answer