def solve():
    """Index: 6270.
    Returns: the total number of wheels in the garage.
    """
    # L1
    num_bicycles = 9 # 9 bicycles
    wheels_per_bicycle = 2 # WK
    bicycle_wheels = num_bicycles * wheels_per_bicycle

    # L2
    num_cars = 16 # 16 cars
    wheels_per_car = 4 # WK
    car_wheels = num_cars * wheels_per_car

    # L3
    total_wheels = bicycle_wheels + car_wheels

    # FA
    answer = total_wheels
    return answer