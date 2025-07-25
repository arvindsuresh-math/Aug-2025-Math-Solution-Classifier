def solve():
    """Index: 2253.
    Returns: the amount of money Ines has left after buying peaches.
    """
    # L1
    pounds_peaches = 3 # 3 pounds of peaches
    price_per_pound = 2 # $2 per pound
    total_cost = pounds_peaches * price_per_pound

    # L2
    initial_money = 20 # $20 in her purse
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer