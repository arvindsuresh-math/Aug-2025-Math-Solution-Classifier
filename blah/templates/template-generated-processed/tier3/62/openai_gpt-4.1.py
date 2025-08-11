def solve():
    """Index: 62.
    Returns: the amount of oil each of the remaining cans is holding.
    """
    # L1
    cans_with_8_liters = 10 # 10 of the cans are holding 8 liters each
    liters_per_can = 8 # 8 liters each
    oil_in_10_cans = cans_with_8_liters * liters_per_can

    # L2
    total_oil = 290 # There are 290 liters of oil
    oil_left = total_oil - oil_in_10_cans

    # L3
    total_cans = 24 # 24 cans
    remaining_cans = total_cans - cans_with_8_liters

    # L4
    oil_per_remaining_can = oil_left / remaining_cans

    # FA
    answer = oil_per_remaining_can
    return answer