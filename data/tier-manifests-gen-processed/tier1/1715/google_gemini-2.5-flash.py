def solve():
    """Index: 1715.
    Returns: the amount of money Jeremy has left.
    """
    # L1
    num_jerseys = 5 # 5 jerseys
    cost_per_jersey = 2 # $2 each
    cost_jerseys = num_jerseys * cost_per_jersey

    # L2
    cost_basketball = 18 # basketball that cost $18
    cost_shorts = 8 # shorts that cost $8
    total_cost = cost_jerseys + cost_basketball + cost_shorts

    # L3
    initial_money = 50 # $50 to spend
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer