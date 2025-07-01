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

    #: L2
    remaining_liters = total_liters - liters_per_can_8 # eval: 282 = 290 - 8

    #: L3
    remaining_cans = total_cans - num_cans_with_8_liters # eval: 14 = 24 - 10

    #: L4
    liters_per_remaining_can = remaining_liters / remaining_cans # eval: 20.142857142857142 = 282 / 14

    #: FA
    answer = liters_per_remaining_can
    return answer # eval: return 20.142857142857142
