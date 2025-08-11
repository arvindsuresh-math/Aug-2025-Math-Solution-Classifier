def solve():
    """Index: 2803.
    Returns: the amount of money Todd has left in dollars.
    """
    # L1
    num_candy_bars = 4 # 4 candy bars
    cost_per_candy_bar = 2 # cost $2 each
    total_candy_bar_cost = num_candy_bars * cost_per_candy_bar

    # L2
    initial_money = 20 # Todd has $20
    money_left = initial_money - total_candy_bar_cost

    # FA
    answer = money_left
    return answer