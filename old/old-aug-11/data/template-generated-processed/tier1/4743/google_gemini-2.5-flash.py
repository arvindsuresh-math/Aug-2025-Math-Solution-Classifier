def solve():
    """Index: 4743.
    Returns: the total number of tires changed.
    """
    # L1
    num_motorcycles = 12 # 12 motorcycles
    tires_per_motorcycle = 2 # WK
    motorcycle_tires = num_motorcycles * tires_per_motorcycle

    # L2
    num_cars = 10 # 10 cars
    tires_per_car = 4 # WK
    car_tires = num_cars * tires_per_car

    # L3
    total_tires = motorcycle_tires + car_tires

    # FA
    answer = total_tires
    return answer