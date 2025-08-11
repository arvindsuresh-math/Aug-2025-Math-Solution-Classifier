def solve():
    """Index: 2304.
    Returns: the amount of money Amy has left.
    """
    # L1
    num_dolls = 3 # bought 3 dolls
    cost_per_doll = 1 # each of which cost $1
    cost_of_dolls = num_dolls * cost_per_doll

    # L2
    initial_money = 100 # gave her $100 for her birthday
    money_left = initial_money - cost_of_dolls

    # FA
    answer = money_left
    return answer