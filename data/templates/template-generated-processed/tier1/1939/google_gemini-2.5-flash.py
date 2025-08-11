def solve():
    """Index: 1939.
    Returns: the amount of money Jerome has left.
    """
    # L1
    half_money = 43 # Half of Jerome's money was $43
    multiplier_for_total = 2 # WK
    jerome_total_money = half_money * multiplier_for_total

    # L2
    meg_given = 8 # gave $8 to Meg
    money_after_meg = jerome_total_money - meg_given

    # L3
    bianca_multiplier = 3 # thrice as much to Bianca
    bianca_given = meg_given * bianca_multiplier

    # L4
    money_after_bianca = money_after_meg - bianca_given

    # FA
    answer = money_after_bianca
    return answer