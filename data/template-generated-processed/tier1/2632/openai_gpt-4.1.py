def solve():
    """Index: 2632.
    Returns: the number of additional people that could have ridden with the swim team.
    """
    # L1
    max_per_car = 6 # Each car can hold a maximum of 6 people
    num_cars = 2 # 2 cars
    car_capacity = max_per_car * num_cars

    # L2
    max_per_van = 8 # each van can hold a maximum of 8 people
    num_vans = 3 # 3 vans
    van_capacity = max_per_van * num_vans

    # L3
    total_capacity = car_capacity + van_capacity

    # L4
    people_per_car = 5 # 5 people in each car
    people_in_cars = num_cars * people_per_car

    # L5
    people_per_van = 3 # 3 people in each van
    people_in_vans = num_vans * people_per_van

    # L6
    total_people = people_in_cars + people_in_vans

    # L7
    additional_people = total_capacity - total_people

    # FA
    answer = additional_people
    return answer