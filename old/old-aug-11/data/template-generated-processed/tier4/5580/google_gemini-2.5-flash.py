def solve():
    """Index: 5580.
    Returns: the total number of matchbox vehicles Jude buys.
    """
    # L1
    num_trucks = 10 # buys 10 trucks
    caps_per_truck = 6 # 6 bottle caps for a truck
    cost_trucks_caps = num_trucks * caps_per_truck

    # L2
    initial_caps = 100 # Jude has 100 bottle caps
    remaining_caps_after_trucks = initial_caps - cost_trucks_caps

    # L3
    percent_remaining_on_cars = 0.75 # spends 75% of his remaining bottle caps on cars
    caps_spent_on_cars = remaining_caps_after_trucks * percent_remaining_on_cars

    # L4
    caps_per_car = 5 # 5 bottle caps for a car
    num_cars = caps_spent_on_cars / caps_per_car

    # L5
    total_vehicles = num_trucks + num_cars

    # FA
    answer = total_vehicles
    return answer