def solve():
    """Index: 5119.
    Returns: the total number of tires in the parking lot.
    """
    # L1
    car_tires = 4 # 4-wheel drive cars
    spare_tire = 1 # spare tire
    tires_per_car = car_tires + spare_tire

    # L2
    num_cars = 30 # thirty 4-wheel drive cars
    total_tires = num_cars * tires_per_car

    # FA
    answer = total_tires
    return answer