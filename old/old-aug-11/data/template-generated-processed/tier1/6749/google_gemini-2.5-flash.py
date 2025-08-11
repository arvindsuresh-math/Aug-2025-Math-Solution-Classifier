def solve():
    """Index: 6749.
    Returns: the total number of toys James buys.
    """
    # L1
    multiplier_soldiers = 2 # twice as many toy soldiers
    toy_cars_bought = 20 # He buys 20 toy cars
    toy_soldiers_bought = multiplier_soldiers * toy_cars_bought

    # L2
    total_toys = toy_cars_bought + toy_soldiers_bought

    # FA
    answer = total_toys
    return answer