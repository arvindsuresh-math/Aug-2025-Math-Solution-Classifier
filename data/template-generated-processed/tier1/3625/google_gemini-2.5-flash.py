def solve():
    """Index: 3625.
    Returns: the amount of money Ken will get back.
    """
    # L1
    pounds_of_steak = 2 # two pounds
    price_per_pound = 7 # $7
    cost_of_steak = pounds_of_steak * price_per_pound

    # L2
    payment_amount = 20 # $20 bill
    change_back = payment_amount - cost_of_steak

    # FA
    answer = change_back
    return answer