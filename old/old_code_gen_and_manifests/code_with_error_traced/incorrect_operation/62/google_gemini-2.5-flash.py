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
    oil_in_specific_cans = num_cans_with_specific_capacity + capacity_per_specific_can # eval: 18 = 10 + 8

    #: L2
    remaining_oil_liters = total_oil_liters - oil_in_specific_cans # eval: 272 = 290 - 18

    #: L3
    remaining_cans = total_cans - num_cans_with_specific_capacity # eval: 14 = 24 - 10

    #: L4
    oil_per_remaining_can = remaining_oil_liters / remaining_cans # eval: 19.428571428571427 = 272 / 14

    #: FA
    answer = oil_per_remaining_can
    return answer # eval: return 19.428571428571427
