def solve():
    """Index: 1941.
    Returns: the number of dollars Saheed made.
    """
    # L1
    vika_made = 84 # Vika made $84
    kayla_less_than_vika = 30 # Kayla made $30 less than Vika
    kayla_made = vika_made - kayla_less_than_vika

    # L2
    saheed_multiplier = 4 # four times as much money as Kayla
    saheed_made = saheed_multiplier * kayla_made

    # FA
    answer = saheed_made
    return answer