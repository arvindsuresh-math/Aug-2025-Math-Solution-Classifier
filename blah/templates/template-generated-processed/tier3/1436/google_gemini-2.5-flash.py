def solve():
    """Index: 1436.
    Returns: the combined total number of musical instruments owned by Charlie and Carli.
    """
    # L1
    charlie_flutes = 1 # one flute
    charlie_horns = 2 # two horns
    charlie_harps = 1 # a harp
    charlie_total_instruments = charlie_flutes + charlie_horns + charlie_harps

    # L2
    carli_flute_multiplier = 2 # twice as many flutes
    carli_flutes = carli_flute_multiplier * charlie_flutes

    # L3
    carli_horn_divisor = 2 # half as many horns
    carli_horns = charlie_horns / carli_horn_divisor

    # L4
    carli_total_instruments = carli_flutes + carli_horns

    # L5
    combined_total_instruments = charlie_total_instruments + carli_total_instruments

    # FA
    answer = combined_total_instruments
    return answer