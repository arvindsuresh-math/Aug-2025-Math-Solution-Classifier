def solve():
    """Index: 2253.
    Returns: the amount of money Ines had left.
    """
    # L1
    pounds_of_peaches = 3 # 3 pounds of peaches
    price_per_pound = 2 # $2 per pound
    cost_of_peaches = pounds_of_peaches * price_per_pound

    # L2
    initial_money = 20 # $20 in her purse
    money_left = initial_money - cost_of_peaches

    # FA
    answer = money_left
    return answer