def solve():
    """Index: 977.
    Returns: the total number of wheels Tommy saw.
    """
    # L1
    num_trucks = 12 # 12 trucks
    num_cars = 13 # 13 cars
    total_vehicles = num_trucks + num_cars

    # L2
    wheels_per_vehicle = 4 # 4 wheels
    total_wheels = total_vehicles * wheels_per_vehicle

    # FA
    answer = total_wheels
    return answer