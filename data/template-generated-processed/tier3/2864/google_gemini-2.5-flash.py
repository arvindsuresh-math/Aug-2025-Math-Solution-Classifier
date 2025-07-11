def solve():
    """Index: 2864.
    Returns: the number of more turtles Trey has than Kristen.
    """
    # L1
    kristen_turtles = 12 # Kristen has 12
    kris_fraction_denominator = 4 # 1/4 as many turtles as Kristen
    kris_turtles = kristen_turtles / kris_fraction_denominator

    # L2
    trey_multiplier = 7 # 7 times as many turtles as Kris
    trey_turtles = kris_turtles * trey_multiplier

    # L3
    trey_more_than_kristen = trey_turtles - kristen_turtles

    # FA
    answer = trey_more_than_kristen
    return answer