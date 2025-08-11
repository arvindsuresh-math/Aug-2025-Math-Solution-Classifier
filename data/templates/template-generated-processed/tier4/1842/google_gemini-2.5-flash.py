def solve():
    """Index: 1842.
    Returns: the percentage chance it's a white truck, rounded to the nearest integer.
    """
    # L1
    num_trucks = 50 # 50 trucks
    num_cars = 40 # 40 cars
    total_vehicles = num_trucks + num_cars

    # L2
    red_truck_divisor = 2 # Half the trucks are red
    red_trucks = num_trucks / red_truck_divisor

    # L3
    black_truck_percentage = 0.2 # 20% are black
    black_trucks = num_trucks * black_truck_percentage

    # L4
    white_trucks = num_trucks - red_trucks - black_trucks

    # L5
    percent_multiplier = 100 # WK
    raw_white_truck_percentage = (white_trucks / total_vehicles) * percent_multiplier
    white_truck_percentage = round(raw_white_truck_percentage)

    # FA
    answer = white_truck_percentage
    return answer