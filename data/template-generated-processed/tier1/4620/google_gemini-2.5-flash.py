def solve():
    """Index: 4620.
    Returns: the total number of people needed to lift cars and trucks.
    """
    # L1
    people_per_car = 5 # 5 people to lift a car
    multiplier_for_truck = 2 # twice as many people
    people_per_truck = people_per_car * multiplier_for_truck

    # L2
    num_cars = 6 # 6 cars
    people_for_cars = people_per_car * num_cars

    # L3
    num_trucks = 3 # 3 trucks
    people_for_trucks = people_per_truck * num_trucks

    # L4
    total_people_needed = people_for_cars + people_for_trucks

    # FA
    answer = total_people_needed
    return answer