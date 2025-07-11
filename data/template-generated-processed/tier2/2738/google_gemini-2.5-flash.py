def solve():
    """Index: 2738.
    Returns: the amount of money left in Marj's wallet.
    """
    # L1
    bill_denomination_20 = 20 # two $20 bills
    num_20_bills = 2 # two $20 bills
    amount_from_20_bills = bill_denomination_20 * num_20_bills

    # L2
    bill_denomination_5 = 5 # three $5 bills
    num_5_bills = 3 # three $5 bills
    amount_from_5_bills = bill_denomination_5 * num_5_bills

    # L3
    loose_coins_amount = 4.50 # $4.50 in loose coins
    loose_coins_amount_calc = 4.5 # WK
    total_money_initial = amount_from_20_bills + amount_from_5_bills + loose_coins_amount_calc

    # L4
    cake_cost = 17.50 # cake that costs $17.50
    total_money_initial_calc = 59.5 # WK
    cake_cost_calc = 17.5 # WK
    money_left = total_money_initial_calc - cake_cost_calc

    # FA
    answer = money_left
    return answer