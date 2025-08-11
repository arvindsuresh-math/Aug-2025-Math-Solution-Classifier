def solve():
    """Index: 2304.
    Returns: the amount of money Amy has left after buying the dolls.
    """
    # L1
    num_dolls = 3 # 3 dolls
    cost_per_doll = 1 # each of which cost $1
    total_cost = num_dolls * cost_per_doll

    # L2
    initial_money = 100 # gave her $100 for her birthday
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer