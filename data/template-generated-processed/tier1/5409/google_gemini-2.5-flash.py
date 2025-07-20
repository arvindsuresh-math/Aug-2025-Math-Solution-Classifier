def solve():
    """Index: 5409.
    Returns: the amount of money Bruce has left to buy more clothes.
    """
    # L1
    num_shirts = 5 # 5 shirts
    cost_per_shirt = 5 # $5 each
    cost_shirts = num_shirts * cost_per_shirt

    # L2
    cost_pants = 26 # a pair of pants that cost $26
    total_spent = cost_shirts + cost_pants

    # L3
    initial_money = 71 # $71 to spend on clothes
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer