def solve():
    """Index: 7282.
    Returns: the total amount of money Oliver is left with.
    """
    # L1
    oliver_quarters = 200 # 200 quarters
    quarter_value = 0.25 # WK
    oliver_quarters_value = oliver_quarters * quarter_value

    # L2
    oliver_cash = 40 # $40
    oliver_total_money = oliver_cash + oliver_quarters_value

    # L3
    sister_quarters = 120 # 120 quarters
    sister_quarters_value = sister_quarters * quarter_value

    # L4
    sister_cash = 5 # $5
    total_given_to_sister = sister_quarters_value + sister_cash

    # L5
    oliver_money_left = oliver_total_money - total_given_to_sister

    # FA
    answer = oliver_money_left
    return answer