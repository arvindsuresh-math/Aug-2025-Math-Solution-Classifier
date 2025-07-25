def solve():
    """Index: 1599.
    Returns: the amount of money Natalie has left after shopping.
    """
    # L1
    jumper_cost = 9 # jumper for $9
    tshirt_cost = 4 # T-shirt for $4
    heels_cost = 5 # pair of heels for $5
    total_cost = jumper_cost + tshirt_cost + heels_cost

    # L2
    natalie_money = 26 # Natalie has $26
    money_left = natalie_money - total_cost

    # FA
    answer = money_left
    return answer