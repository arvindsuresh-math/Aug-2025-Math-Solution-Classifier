def solve():
    """Index: 294.
    Returns: the amount of money Phillip has left after shopping.
    """
    # L1
    oranges_cost = 14 # spent $14 on oranges
    apples_cost = 25 # spent $25 on apples
    candy_cost = 6 # spent $6 on candy
    total_spent = oranges_cost + apples_cost + candy_cost

    # L2
    initial_money = 95 # gave him $95
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer