def solve(
        total_oil_liters: int = 290, # There are 290 liters of oil
        total_cans: int = 24, # in 24 cans
        cans_with_known_volume: int = 10, # If 10 of the cans
        volume_per_known_can: int = 8 # are holding 8 liters each
    ):
    """Index: 62.
    Returns: the amount of oil each of the remaining cans is holding.
    """
    #: L1
    oil_in_known_cans = cans_with_known_volume * volume_per_known_can

    #: L2
    remaining_oil_liters = total_oil_liters - oil_in_known_cans

    #: L3
    remaining_cans = total_cans - cans_with_known_volume

    #: L4
    oil_per_remaining_can = remaining_oil_liters / remaining_cans

    answer = oil_per_remaining_can # FINAL ANSWER
    return answer