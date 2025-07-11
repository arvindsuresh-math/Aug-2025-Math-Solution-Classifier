def solve():
    """Index: 1939.
    Returns: the amount of money Jerome has left after giving money to Meg and Bianca.
    """
    # L1
    half_money = 43 # Half of Jerome's money was $43
    jerome_total = half_money * 2

    # L2
    meg_given = 8 # he gave $8 to Meg
    after_meg = jerome_total - meg_given

    # L3
    bianca_multiplier = 3 # thrice as much to Bianca
    bianca_given = meg_given * bianca_multiplier

    # L4
    after_bianca = after_meg - bianca_given

    # FA
    answer = after_bianca
    return answer