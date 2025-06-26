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
    liters_in_8_liter_cans = num_cans_with_8_liters * liters_per_can_8

    #: L2
    remaining_liters = total_liters - liters_in_8_liter_cans

    #: L3
    remaining_cans = total_cans - num_cans_with_8_liters

    #: L4
    liters_per_remaining_can = remaining_liters / remaining_cans

    answer = liters_per_remaining_can # FINAL ANSWER
    return answer