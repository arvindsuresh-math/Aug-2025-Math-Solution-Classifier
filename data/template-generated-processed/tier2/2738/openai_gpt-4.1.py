def solve():
    """Index: 2738.
    Returns: the amount of money left in Marj's wallet after buying the cake.
    """
    # L1
    bill_20_value = 20 # $20 bills
    bill_20_count = 2 # two $20 bills
    total_20_bills = bill_20_value * bill_20_count

    # L2
    bill_5_value = 5 # $5 bills
    bill_5_count = 3 # three $5 bills
    total_5_bills = bill_5_value * bill_5_count

    # L3
    loose_coins = 4.5 # $4.50 in loose coins
    total_money = total_20_bills + total_5_bills + loose_coins

    # L4
    cake_cost = 17.5 # cake that costs $17.50
    money_left = total_money - cake_cost

    # FA
    answer = money_left
    return answer