def solve():
    """Index: 1703.
    Returns: how much more coach A spent than coach B.
    """
    # L1
    basketball_price = 29 # $29 each
    basketball_qty = 10 # ten new basketballs
    coach_a_total = basketball_price * basketball_qty

    # L2
    baseball_price = 2.5 # $2.50 each
    baseball_qty = 14 # 14 new baseballs
    coach_b_baseballs_total = baseball_price * baseball_qty

    # L3
    bat_price = 18 # a baseball bat for $18
    coach_b_total = coach_b_baseballs_total + bat_price

    # L4
    difference = coach_a_total - coach_b_total

    # FA
    answer = difference
    return answer