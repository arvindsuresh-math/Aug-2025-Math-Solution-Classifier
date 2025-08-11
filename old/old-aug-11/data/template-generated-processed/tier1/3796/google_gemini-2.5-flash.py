def solve():
    """Index: 3796.
    Returns: the amount of money Donny has left.
    """
    # L1
    initial_money = 78 # $78 in his piggy bank
    kite_cost = 8 # a kite for $8
    money_after_kite = initial_money - kite_cost

    # L2
    frisbee_cost = 9 # a frisbee for $9
    money_left = money_after_kite - frisbee_cost

    # FA
    answer = money_left
    return answer