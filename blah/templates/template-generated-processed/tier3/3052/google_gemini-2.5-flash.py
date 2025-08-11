def solve():
    """Index: 3052.
    Returns: the amount of money Hannah has left.
    """
    # L1
    initial_money = 30 # Hannah brought $30 to the county fair
    rides_divisor = 2 # spent half of it
    spent_on_rides = initial_money / rides_divisor

    # L2
    dessert_cost = 5 # another $5 on dessert
    total_spent = spent_on_rides + dessert_cost

    # L3
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer