def solve():
    """Index: 1675.
    Returns: the total weight of the lorry after being loaded.
    """
    # L1
    num_bags = 20 # 20 bags of apples
    weight_per_bag = 60 # each weighing 60 pounds
    additional_weight = num_bags * weight_per_bag

    # L2
    empty_lorry_weight = 500 # 500 pounds when empty
    total_weight = empty_lorry_weight + additional_weight

    # FA
    answer = total_weight
    return answer