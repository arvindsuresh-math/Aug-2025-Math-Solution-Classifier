def solve():
    """Index: 1346.
    Returns: the number of green toads per acre.
    """
    # L1
    spotted_brown_toads_per_acre = 50 # 50 spotted brown toads per acre
    quarter_multiplier = 4 # one-quarter of the brown toads
    total_brown_toads_per_acre = spotted_brown_toads_per_acre * quarter_multiplier

    # L2
    brown_toads_per_green_toad = 25 # 25 brown toads
    green_toads_per_acre = total_brown_toads_per_acre / brown_toads_per_green_toad

    # FA
    answer = green_toads_per_acre
    return answer