def solve():
    """Index: 6751.
    Returns: the initial amount of money Dennis had.
    """
    # L1
    value_of_10_dollar_bill = 10 # WK
    num_10_dollar_bills = 2 # 2 $10 bills
    change_from_10_dollar_bills = value_of_10_dollar_bill * num_10_dollar_bills

    # L2
    loose_coins_change = 3 # $3 in loose coins
    total_change = change_from_10_dollar_bills + loose_coins_change

    # L3
    cost_of_shirts = 27 # shirts worth $27
    initial_money = cost_of_shirts + total_change

    # FA
    answer = initial_money
    return answer