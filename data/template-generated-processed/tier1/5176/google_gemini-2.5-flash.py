def solve():
    """Index: 5176.
    Returns: the total weight the bridge must hold up.
    """
    # L1
    num_soda_cans = 6 # 6 cans of soda
    ounces_per_can_soda = 12 # 12 ounces of soda
    weight_soda = num_soda_cans * ounces_per_can_soda

    # L2
    initial_cans = 6 # 6 cans of soda
    additional_empty_cans = 2 # 2 more empty cans
    total_empty_cans = initial_cans + additional_empty_cans

    # L3
    weight_empty_can = 2 # 2 ounces empty
    weight_empty_cans = total_empty_cans * weight_empty_can

    # L4
    total_weight = weight_soda + weight_empty_cans

    # FA
    answer = total_weight
    return answer