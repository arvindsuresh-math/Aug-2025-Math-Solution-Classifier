def solve():
    """Index: 6494.
    Returns: the total weight of Donna's fully loaded truck.
    """
    # L1
    num_soda_crates = 20 # 20 crates of soda
    weight_per_soda_crate = 50 # each weigh 50 pounds
    total_soda_weight = num_soda_crates * weight_per_soda_crate

    # L2
    multiplier_for_produce = 2 # twice as much weight in fresh produce as in soda
    total_produce_weight = total_soda_weight * multiplier_for_produce

    # L3
    num_dryers = 3 # 3 dryers
    weight_per_dryer = 3000 # each weigh 3000 pounds
    total_dryer_weight = num_dryers * weight_per_dryer

    # L4
    empty_truck_weight = 12000 # empty truck weighs 12,000 pounds
    fully_loaded_truck_weight = empty_truck_weight + total_soda_weight + total_produce_weight + total_dryer_weight

    # FA
    answer = fully_loaded_truck_weight
    return answer