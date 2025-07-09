def solve(
    total_liters: int = 290, # There are 290 liters of oil
    total_cans: int = 24, # in 24 cans
    num_cans_with_8_liters: int = 10, # If 10 of the cans are holding 8 liters each
    liters_per_can_8: int = 8 # 8 liters each
):
    """Index: 62.
    Returns: the amount of oil each of the remaining cans is holding.
    """

    #: L1
    liters_in_8_liter_cans = num_cans_with_8_liters * liters_per_can_8 # eval: 80 = 10 * 8

    #: L2
    remaining_liters = total_liters - liters_in_8_liter_cans # eval: 210 = 290 - 80

    #: L3
    remaining_cans = 15 # eval: 15 = 15

    #: L4
    liters_per_remaining_can = remaining_liters / remaining_cans # eval: 14.0 = 210 / 15

    #: FA
    answer = liters_per_remaining_can
    return answer # eval: return 14.0
