def solve():
    """Index: 5611.
    Returns: the total number of people who went on the hike.
    """
    # L1
    num_cars = 3 # 3 cars
    people_per_car = 4 # 4 people in each car
    people_in_cars = num_cars * people_per_car

    # L2
    num_taxis = 6 # 6 taxis
    people_per_taxi = 6 # 6 people in each taxis
    people_in_taxis = num_taxis * people_per_taxi

    # L3
    num_vans = 2 # 2 vans
    people_per_van = 5 # 5 people in each van
    people_in_vans = num_vans * people_per_van

    # L4
    total_people = people_in_cars + people_in_taxis + people_in_vans

    # FA
    answer = total_people
    return answer