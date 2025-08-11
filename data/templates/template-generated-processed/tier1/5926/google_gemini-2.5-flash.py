def solve():
    """Index: 5926.
    Returns: the total amount Jack has in yen.
    """
    # L1
    euros_jack_has = 11 # 11 euros
    pounds_per_euro = 2 # 2 pounds per euro
    euros_to_pounds = euros_jack_has * pounds_per_euro

    # L2
    pounds_jack_has = 42 # 42 pounds
    total_pounds = euros_to_pounds + pounds_jack_has

    # L3
    yen_per_pound = 100 # 100 yen per pound
    pounds_to_yen = total_pounds * yen_per_pound

    # L4
    yen_jack_has = 3000 # 3000 yen
    total_yen = pounds_to_yen + yen_jack_has

    # FA
    answer = total_yen
    return answer