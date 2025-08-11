def solve():
    """Index: 250.
    Returns: how heavy the weights felt when being lowered.
    """
    # L1
    num_plates = 10 # 10 weight plates
    weight_per_plate = 30 # each weighing 30 pounds
    total_weight_stack = num_plates * weight_per_plate

    # L2
    heavier_percentage = 0.2 # 20% heavier
    added_weight = total_weight_stack * heavier_percentage

    # L3
    felt_weight = total_weight_stack + added_weight

    # FA
    answer = felt_weight
    return answer