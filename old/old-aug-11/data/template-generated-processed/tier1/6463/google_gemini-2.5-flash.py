def solve():
    """Index: 6463.
    Returns: the total number of toy cars made by the factory.
    """
    # L1
    cars_yesterday = 60 # made 60 cars yesterday
    multiplier_today = 2 # twice the number of cars
    cars_today = cars_yesterday * multiplier_today

    # L2
    total_cars = cars_yesterday + cars_today

    # FA
    answer = total_cars
    return answer