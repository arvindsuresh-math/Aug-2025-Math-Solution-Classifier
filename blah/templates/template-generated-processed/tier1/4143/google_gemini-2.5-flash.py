def solve():
    """Index: 4143.
    Returns: the total number of people in the cars by the end of the race.
    """
    # L1
    passengers_per_car_initial = 2 # 2 passengers
    driver_per_car = 1 # a driver
    people_per_car_initial = passengers_per_car_initial + driver_per_car

    # L2
    num_cars = 20 # 20 cars
    total_people_initial = num_cars * people_per_car_initial

    # L3
    additional_passenger_per_car = 1 # each car gains another passenger
    additional_people_halfway = num_cars * additional_passenger_per_car

    # L4
    total_people_end_of_race = total_people_initial + additional_people_halfway

    # FA
    answer = total_people_end_of_race
    return answer