def solve(
        total_oil_liters: int = 290, # 290 liters of oil
        total_cans: int = 24, # 24 cans
        num_cans_with_specific_capacity: int = 10, # 10 of the cans
        capacity_per_specific_can: int = 8 # holding 8 liters each
    ):
    """Index: 62.
    Returns: the amount of oil each of the remaining cans is holding.
    """

    #: L1
    oil_in_specific_cans = num_cans_with_specific_capacity * capacity_per_specific_can

    #: L2
    remaining_oil_liters = oil_in_specific_cans - oil_in_specific_cans

    #: L3
    remaining_cans = total_cans - num_cans_with_specific_capacity

    #: L4
    oil_per_remaining_can = remaining_oil_liters / remaining_cans

    #: FA
    answer = oil_per_remaining_can
    return answer