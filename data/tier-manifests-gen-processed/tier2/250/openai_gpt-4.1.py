def solve():
    """Index: 250.
    Returns: the weight the plates felt like when being lowered.
    """
    # L1
    num_plates = 10 # Tom uses 10 weight plates
    plate_weight = 30 # each weighing 30 pounds
    total_weight = num_plates * plate_weight

    # L2
    added_percent = 0.2 # 20% heavier on the lowering portion
    added_weight = total_weight * added_percent

    # L3
    lowered_weight = total_weight + added_weight

    # FA
    answer = lowered_weight
    return answer