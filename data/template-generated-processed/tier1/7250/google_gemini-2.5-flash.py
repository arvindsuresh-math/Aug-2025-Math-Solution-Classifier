def solve():
    """Index: 7250.
    Returns: the total number of car wheels in the parking lot.
    """
    # L1
    num_guest_cars = 10 # 10 cars that they park in the parking lot
    wheels_per_car = 4 # If each car has 4 wheels
    guest_car_wheels = num_guest_cars * wheels_per_car

    # L2
    num_parents_cars = 2 # her car and her husband's jeep
    parents_car_wheels = num_parents_cars * wheels_per_car

    # L3
    total_wheels = guest_car_wheels + parents_car_wheels

    # FA
    answer = total_wheels
    return answer