def solve():
    """Index: 1703.
    Returns: how much more Coach A spent than Coach B.
    """
    # L1
    basketball_price = 29 # $29 each
    num_basketballs = 10 # ten new basketballs
    coach_a_total_spend = basketball_price * num_basketballs

    # L2
    baseball_price_text = 2.50 # $2.50 each
    baseball_price_calc = 2.5 # from solution text: 2.5*14
    num_baseballs = 14 # 14 new baseballs
    coach_b_baseballs_spend = baseball_price_calc * num_baseballs

    # L3
    baseball_bat_price = 18 # a baseball bat for $18
    coach_b_total_spend = coach_b_baseballs_spend + baseball_bat_price

    # L4
    difference_in_spend = coach_a_total_spend - coach_b_total_spend

    # FA
    answer = difference_in_spend
    return answer