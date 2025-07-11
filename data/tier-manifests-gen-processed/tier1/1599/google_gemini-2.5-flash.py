def solve():
    """Index: 1599.
    Returns: the amount of money Natalie has left.
    """
    # L1
    jumper_cost = 9 # bought a jumper for $9
    tshirt_cost = 4 # a T-shirt for $4
    heels_cost = 5 # a pair of heels for $5
    total_cost = jumper_cost + tshirt_cost + heels_cost

    # L2
    initial_money = 26 # Natalie has $26 to go shopping
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer