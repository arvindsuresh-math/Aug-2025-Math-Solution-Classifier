def solve():
    """Index: 2632.
    Returns: how many more people could have ridden with the swim team.
    """
    # L1
    max_capacity_per_car = 6 # maximum of 6 people
    num_cars = 2 # 2 cars
    max_car_capacity_total = max_capacity_per_car * num_cars

    # L2
    max_capacity_per_van = 8 # maximum of 8 people
    num_vans = 3 # 3 vans
    max_van_capacity_total = max_capacity_per_van * num_vans

    # L3
    total_max_capacity = max_car_capacity_total + max_van_capacity_total

    # L4
    people_per_car_actual = 5 # 5 people in each car
    people_in_cars_actual = num_cars * people_per_car_actual

    # L5
    people_per_van_actual = 3 # 3 people in each van
    people_in_vans_actual = num_vans * people_per_van_actual

    # L6
    total_people_actual = people_in_cars_actual + people_in_vans_actual

    # L7
    additional_people_possible = total_max_capacity - total_people_actual

    # FA
    answer = additional_people_possible
    return answer