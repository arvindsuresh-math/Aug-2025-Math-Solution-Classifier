def solve():
    """Index: 1941.
    Returns: the number of dollars Saheed made.
    """
    # L1
    vika_money = 84 # Vika made $84
    kayla_less_than_vika = 30 # $30 less than Vika
    kayla_money = vika_money - kayla_less_than_vika

    # L2
    saheed_multiplier = 4 # four times as much money as Kayla
    saheed_money = saheed_multiplier * kayla_money

    # FA
    answer = saheed_money
    return answer