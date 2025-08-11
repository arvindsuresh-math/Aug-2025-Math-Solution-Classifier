def solve():
    """Index: 2642.
    Returns: the cost of a pair of socks.
    """
    # L1
    initial_money = 100 # George had $100
    shirt_cost = 24 # bought a shirt for $24
    money_after_shirt = initial_money - shirt_cost

    # L2
    money_left_after_socks = 65 # he had $65 left
    socks_cost = money_after_shirt - money_left_after_socks

    # FA
    answer = socks_cost
    return answer