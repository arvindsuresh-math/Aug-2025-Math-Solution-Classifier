def solve():
    """Index: 6131.
    Returns: the total number of passengers James has seen today.
    """
    # L1
    num_trucks = 12 # 12 trucks
    people_per_truck = 2 # trucks held 2 people each
    people_in_trucks = num_trucks * people_per_truck

    # L2
    num_buses = 2 # a couple of buses
    people_per_bus = 15 # buses held 15 people each
    people_in_buses = num_buses * people_per_bus

    # L3
    multiplier_for_taxis = 2 # twice as many taxis
    num_taxis = multiplier_for_taxis * num_buses

    # L4
    people_per_taxi = 2 # taxis held 2 people each
    people_in_taxis = num_taxis * people_per_taxi

    # L5
    num_cars = 30 # 30 cars
    people_per_car = 3 # cars held 3 people each
    people_in_cars = num_cars * people_per_car

    # L6
    total_vehicles_counted = 52 # counted 52 vehicles so far today
    num_motorbikes = total_vehicles_counted - num_trucks - num_buses - num_taxis - num_cars

    # L7
    people_per_motorbike = 1 # motorbikes held 1 person each
    people_on_motorbikes = num_motorbikes * people_per_motorbike

    # L8
    total_passengers = people_in_trucks + people_in_buses + people_in_taxis + people_in_cars + people_on_motorbikes

    # FA
    answer = total_passengers
    return answer