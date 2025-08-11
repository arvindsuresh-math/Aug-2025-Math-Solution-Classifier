def solve():
    """Index: 5512.
    Returns: the total number of turtles altogether.
    """
    # L1
    kristen_turtles = 12 # Kristen has 12
    kris_fraction_denominator = 4 # one fourth the turtles Kristen has
    kris_turtles = kristen_turtles / kris_fraction_denominator

    # L2
    trey_multiplier = 5 # 5 times as many turtles as Kris
    trey_turtles = kris_turtles * trey_multiplier

    # L3
    total_turtles = kristen_turtles + kris_turtles + trey_turtles

    # FA
    answer = total_turtles
    return answer