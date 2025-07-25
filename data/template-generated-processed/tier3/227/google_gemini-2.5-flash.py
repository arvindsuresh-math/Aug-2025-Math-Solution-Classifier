def solve():
    """Index: 227.
    Returns: the amount of money Ian has left after paying off debts.
    """
    # L1
    initial_money = 100 # Ian won $100 in the lottery
    paid_to_colin = 20 # He paid $20 to Colin
    money_after_colin = initial_money - paid_to_colin

    # L2
    multiplier_helen = 2 # twice as much
    paid_to_helen = multiplier_helen * paid_to_colin

    # L3
    money_after_helen = money_after_colin - paid_to_helen

    # L4
    divisor_benedict = 2 # half as much
    paid_to_benedict = paid_to_helen / divisor_benedict

    # L5
    money_left = money_after_helen - paid_to_benedict

    # FA
    answer = money_left
    return answer