def solve():
    """Index: 2794.
    Returns: the total amount of money John makes repairing cars.
    """
    # L1
    num_cars_40min = 3 # 3 of the cars take 40 minutes each
    time_per_40min_car = 40 # 40 minutes each
    total_time_40min_cars = num_cars_40min * time_per_40min_car

    # L2
    total_cars = 5 # John repairs 5 cars
    num_other_cars = total_cars - num_cars_40min

    # L3
    percent_longer = 0.5 # 50% longer each to repair
    extra_time_per_other_car = time_per_40min_car * percent_longer

    # L4
    time_per_other_car = time_per_40min_car + extra_time_per_other_car

    # L5
    total_time_all_cars = total_time_40min_cars + num_other_cars * time_per_other_car

    # L6
    minutes_per_hour = 60 # WK
    total_hours = total_time_all_cars / minutes_per_hour

    # L7
    wage_per_hour = 20 # $20 per hour
    total_money = total_hours * wage_per_hour

    # FA
    answer = total_money
    return answer