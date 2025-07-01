def solve(
    total_liters: int = 290,  # There are 290 liters of oil in total
    total_cans: int = 24,  # in 24 cans
    known_cans: int = 10,  # 10 of the cans are holding 8 liters each
    known_can_volume: int = 8  # each of these 10 cans holds 8 liters
):
    """Index: 62.
    Returns: the amount of oil in each of the remaining cans."""

    #: L1

    #: L2
    remaining_liters = total_liters - total_cans # eval: 266 = 290 - 24

    #: L3
    remaining_cans = total_cans - known_cans # eval: 14 = 24 - 10

    #: L4
    remaining_can_volume = remaining_liters / remaining_cans # eval: 19.0 = 266 / 14

    #: FA
    answer = remaining_can_volume
    return answer # eval: return 19.0
