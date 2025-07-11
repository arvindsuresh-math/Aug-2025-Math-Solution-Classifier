def solve():
    """Index: 1842.
    Returns: the percentage chance a randomly picked vehicle is a white truck, rounded to the nearest integer.
    """
    # L1
    num_trucks = 50 # 50 trucks
    num_cars = 40 # 40 cars
    total_vehicles = num_trucks + num_cars

    # L2
    red_truck_divisor = 2 # half the trucks are red
    num_red_trucks = num_trucks / red_truck_divisor

    # L3
    black_truck_percent = 0.2 # 20% are black
    num_black_trucks = num_trucks * black_truck_percent

    # L4
    num_white_trucks = num_trucks - num_red_trucks - num_black_trucks

    # L5
    percent_multiplier = 100 # WK
    percent_white_trucks = num_white_trucks / total_vehicles * percent_multiplier
    # FA
    answer = round(percent_white_trucks)
    return answer