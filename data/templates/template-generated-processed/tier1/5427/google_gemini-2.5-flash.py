def solve():
    """Index: 5427.
    Returns: the amount of change Blake was given.
    """
    # L1
    oranges_cost = 40 # spends $40 on oranges
    apples_cost = 50 # $50 on apples
    mangoes_cost = 60 # $60 on mangoes
    total_fruit_cost = oranges_cost + apples_cost + mangoes_cost

    # L2
    initial_money = 300 # he has $300
    change_given = initial_money - total_fruit_cost

    # FA
    answer = change_given
    return answer