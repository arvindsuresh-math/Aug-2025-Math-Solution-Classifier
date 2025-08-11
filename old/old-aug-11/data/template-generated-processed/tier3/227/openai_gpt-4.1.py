def solve():
    """Index: 227.
    Returns: the amount of money Ian has left after paying off debts.
    """
    # L1
    initial_money = 100 # Ian won $100 in the lottery
    colin_payment = 20 # He paid $20 to Colin
    after_colin = initial_money - colin_payment

    # L2
    helen_multiplier = 2 # Twice as much to Helen
    helen_payment = helen_multiplier * colin_payment

    # L3
    after_helen = after_colin - helen_payment

    # L4
    benedict_divisor = 2 # Half as much to Benedict
    benedict_payment = helen_payment / benedict_divisor

    # L5
    after_benedict = after_helen - benedict_payment

    # FA
    answer = after_benedict
    return answer