def solve():
    """Index: 2840.
    Returns: the number of motorcycles in the parking lot.
    """
    # L1
    num_cars = 19 # 19 cars in the parking lot
    wheels_per_car = 5 # Each car has 5 wheels
    car_wheels = wheels_per_car * num_cars

    # L2
    total_wheels = 117 # Altogether all vehicles have 117 wheels
    motorcycle_wheels = total_wheels - car_wheels

    # L3
    wheels_per_motorcycle = 2 # each motorcycle has 2 wheels
    num_motorcycles = motorcycle_wheels / wheels_per_motorcycle

    # FA
    answer = num_motorcycles
    return answer