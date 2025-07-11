def solve():
    """Index: 564.
    Returns: how much more money Jessica has than Rodney.
    """
    # L1
    jessica_money = 100 # Jessica has 100 dollars
    ian_divisor = 2 # Ian has half as much money as Jessica
    ian_money = jessica_money / ian_divisor

    # L2
    rodney_difference = 35 # Rodney has 35 dollars more than Ian
    rodney_money = ian_money + rodney_difference

    # L3
    jessica_vs_rodney = jessica_money - rodney_money

    # FA
    answer = jessica_vs_rodney
    return answer