def solve():
    """Index: 758.
    Returns: the amount of change Faith will receive.
    """
    # L1
    cake_stand_cost = 28 # cake stand that costs $28
    flour_cost = 5 # flour that cost $5
    total_cost_items = cake_stand_cost + flour_cost

    # L2
    value_of_20_bill = 20 # WK
    num_20_bills = 2 # two $20 bills
    total_from_20_bills = value_of_20_bill * num_20_bills

    # L3
    loose_coins = 3 # $3 in loose coins
    total_paid = total_from_20_bills + loose_coins

    # L4
    change_received = total_paid - total_cost_items

    # FA
    answer = change_received
    return answer