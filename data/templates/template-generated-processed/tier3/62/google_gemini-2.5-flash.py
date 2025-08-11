def solve():
    """Index: 62.
    Returns: the amount of oil each of the remaining cans is holding.
    """
    # L1
    num_cans_group1 = 10 # 10 of the cans
    liters_per_can_group1 = 8 # holding 8 liters each
    total_liters_group1 = num_cans_group1 * liters_per_can_group1

    # L2
    total_oil_initial = 290 # 290 liters of oil
    remaining_oil = total_oil_initial - total_liters_group1

    # L3
    total_cans_initial = 24 # 24 cans
    remaining_cans = total_cans_initial - num_cans_group1

    # L4
    liters_per_remaining_can = remaining_oil / remaining_cans

    # FA
    answer = liters_per_remaining_can
    return answer