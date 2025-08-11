def solve():
    """Index: 5272.
    Returns: the total amount of money on all the tables.
    """
    # L1
    money_more_C_than_A = 20 # $20 more than table A
    money_on_A = 40 # $40 on table A
    money_on_C = money_more_C_than_A + money_on_A

    # L2
    money_on_A_and_C = money_on_C + money_on_A

    # L3
    multiplier_B_vs_C = 2 # twice as much money
    money_on_B = money_on_C * multiplier_B_vs_C

    # L4
    total_money = money_on_B + money_on_A_and_C

    # FA
    answer = total_money
    return answer