def solve():
    """Index: 1715.
    Returns: the amount of money Jeremy has left after his purchases.
    """
    # L1
    num_jerseys = 5 # 5 jerseys
    cost_per_jersey = 2 # $2 each
    jerseys_cost = num_jerseys * cost_per_jersey

    # L2
    basketball_cost = 18 # basketball that cost $18
    shorts_cost = 8 # shorts that cost $8
    total_spent = jerseys_cost + basketball_cost + shorts_cost

    # L3
    initial_money = 50 # $50 to spend
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer