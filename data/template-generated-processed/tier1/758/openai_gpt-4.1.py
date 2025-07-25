def solve():
    """Index: 758.
    Returns: the amount of change Faith will receive.
    """
    # L1
    flour_cost = 5 # flour that cost $5
    cake_stand_cost = 28 # cake stand that costs $28
    total_cost = cake_stand_cost + flour_cost

    # L2
    bill_value = 20 # $20 bills
    num_bills = 2 # two $20 bills
    bills_total = bill_value * num_bills

    # L3
    loose_coins = 3 # $3 in loose coins
    total_given = bills_total + loose_coins

    # L4
    change = total_given - total_cost

    # FA
    answer = change
    return answer