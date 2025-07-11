def solve():
    """Index: 564.
    Returns: the difference in money between Jessica and Rodney.
    """
    # L1
    jessica_money = 100 # Jessica has 100 dollars
    half_divisor = 2 # Ian has half as much money as Jessica
    ian_money = jessica_money / half_divisor

    # L2
    rodney_more_than_ian = 35 # Rodney has 35 dollars more than Ian
    rodney_money = ian_money + rodney_more_than_ian

    # L3
    difference_jessica_rodney = jessica_money - rodney_money

    # FA
    answer = difference_jessica_rodney
    return answer