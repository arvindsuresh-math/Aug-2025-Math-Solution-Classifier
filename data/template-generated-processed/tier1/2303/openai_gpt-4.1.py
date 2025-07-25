def solve():
    """Index: 2303.
    Returns: the number of water balloons Cynthia has.
    """
    # L1
    janice_balloons = 6 # Janice throws all 6 of her water balloons
    randy_fraction_of_janice = 0.5 # Randy has only half as many water balloons as his daughter, Janice
    randy_balloons = randy_fraction_of_janice * janice_balloons

    # L2
    cynthia_multiplier = 4 # Cynthia has four times as many water balloons as her husband, Randy
    cynthia_balloons = cynthia_multiplier * randy_balloons

    # FA
    answer = cynthia_balloons
    return answer