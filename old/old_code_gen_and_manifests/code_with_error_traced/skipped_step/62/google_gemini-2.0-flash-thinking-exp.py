def solve(
    total_oil_liters: int = 290, # There are 290 liters of oil
    total_cans: int = 24, # in 24 cans
    num_cans_holding_specific_amount: int = 10, # If 10 of the cans are holding
    liters_per_specific_can: int = 8 # 8 liters each
):
    """Index: 62.
    Returns: the amount of oil each of the remaining cans is holding.
    """

    #: L1
    oil_in_specific_cans = num_cans_holding_specific_amount * liters_per_specific_can # eval: 80 = 10 * 8

    #: L2

    #: L3
    remaining_cans = total_cans - num_cans_holding_specific_amount # eval: 14 = 24 - 10

    #: L4
    liters_per_remaining_can = num_cans_holding_specific_amount / remaining_cans # eval: 0.7142857142857143 = 10 / 14

    #: FA
    answer = liters_per_remaining_can
    return answer # eval: return 0.7142857142857143
