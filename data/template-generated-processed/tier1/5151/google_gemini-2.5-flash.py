def solve():
    """Index: 5151.
    Returns: the number of cars in the parking lot now.
    """
    # L1
    initial_cars = 80 # 80 cars in a parking lot
    cars_left = 13 # 13 cars left the parking lot
    cars_after_leaving = initial_cars - cars_left

    # L2
    more_cars_than_left = 5 # 5 more cars went in than left
    cars_entered = cars_left + more_cars_than_left

    # L3
    final_cars = cars_after_leaving + cars_entered

    # FA
    answer = final_cars
    return answer