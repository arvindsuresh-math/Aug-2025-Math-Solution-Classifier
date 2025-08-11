def solve():
    """Index: 7432.
    Returns: the total number of hours Mike worked.
    """
    # L1
    time_per_wash = 10 # 10 minutes to wash a car
    num_cars_washed = 9 # washes 9 cars
    time_washing_cars = time_per_wash * num_cars_washed

    # L2
    time_per_oil_change = 15 # 15 minutes to change oil
    num_oil_changes = 6 # changes the oil on 6 cars
    time_changing_oil = time_per_oil_change * num_oil_changes

    # L3
    num_tire_sets = 2 # changes two sets of tires
    time_per_tire_set = 30 # 30 minutes to change a set of tires
    time_changing_tires = num_tire_sets * time_per_tire_set

    # L4
    total_minutes_worked = time_washing_cars + time_changing_oil + time_changing_tires

    # L5
    minutes_per_hour = 60 # WK
    total_hours_worked = total_minutes_worked / minutes_per_hour

    # FA
    answer = total_hours_worked
    return answer