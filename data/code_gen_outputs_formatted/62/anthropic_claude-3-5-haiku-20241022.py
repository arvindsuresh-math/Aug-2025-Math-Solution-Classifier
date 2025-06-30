def solve(
    total_liters: int = 290,  # There are 290 liters of oil in total
    total_cans: int = 24,  # in 24 cans
    known_cans: int = 10,  # 10 of the cans are holding 8 liters each
    known_can_volume: int = 8  # each of these 10 cans holds 8 liters
):
    """Index: 62.
    Returns: the amount of oil in each of the remaining cans."""

    #: L1
    known_cans_total_volume = known_cans * known_can_volume

    #: L2
    remaining_liters = total_liters - known_cans_total_volume

    #: L3
    remaining_cans = total_cans - known_cans

    #: L4
    remaining_can_volume = remaining_liters / remaining_cans

    #: FA
    answer = remaining_can_volume
    return answer