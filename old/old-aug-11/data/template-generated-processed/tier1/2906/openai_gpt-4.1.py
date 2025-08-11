def solve():
    """Index: 2906.
    Returns: the total number of wheels in the garage.
    """
    # L1
    wheels_per_bicycle = 2 # WK
    num_bicycles = 20 # 20 bicycles
    bicycle_wheels = wheels_per_bicycle * num_bicycles

    # L2
    wheels_per_car = 4 # WK
    num_cars = 10 # 10 cars
    car_wheels = wheels_per_car * num_cars

    # L3
    wheels_per_motorcycle = 2 # WK
    num_motorcycles = 5 # 5 motorcycles
    motorcycle_wheels = wheels_per_motorcycle * num_motorcycles

    # L4
    total_wheels = bicycle_wheels + car_wheels + motorcycle_wheels

    # FA
    answer = total_wheels
    return answer