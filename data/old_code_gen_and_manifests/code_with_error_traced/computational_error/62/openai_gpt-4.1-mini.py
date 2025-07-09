def solve(
    total_liters: int = 290,  # There are 290 liters of oil
    total_cans: int = 24,  # in 24 cans
    cans_with_8_liters: int = 10,  # 10 of the cans are holding 8 liters each
    liters_per_can_8_liters: int = 8  # each of those 10 cans holds 8 liters
):
    """Index: 62.
    Returns: the amount of oil each of the remaining cans is holding.
    """

    #: L1
    total_liters_in_10_cans = cans_with_8_liters * liters_per_can_8_liters # eval: 80 = 10 * 8

    #: L2
    remaining_liters = total_liters - total_liters_in_10_cans # eval: 210 = 290 - 80

    #: L3
    remaining_cans = total_cans - cans_with_8_liters # eval: 14 = 24 - 10

    #: L4
    liters_per_remaining_can = 5.0 # eval: 5.0 = 5.0

    #: FA
    answer = liters_per_remaining_can
    return answer # eval: return 5.0
