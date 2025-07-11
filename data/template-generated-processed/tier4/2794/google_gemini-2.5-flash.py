def solve():
    """Index: 2794.
    Returns: the total money John makes repairing cars.
    """
    # L1
    num_cars_group1 = 3 # 3 of the cars
    time_per_car_group1 = 40 # 40 minutes each to repair
    total_time_group1 = num_cars_group1 * time_per_car_group1

    # L2
    total_cars = 5 # 5 cars
    num_cars_group2 = total_cars - num_cars_group1

    # L3
    longer_percent = 0.5 # 50% longer
    extra_time_per_car_group2 = time_per_car_group1 * longer_percent

    # L4
    time_per_car_group2 = time_per_car_group1 + extra_time_per_car_group2

    # L5
    total_repair_minutes = total_time_group1 + num_cars_group2 * time_per_car_group2

    # L6
    minutes_per_hour = 60 # WK
    total_repair_hours = total_repair_minutes / minutes_per_hour

    # L7
    hourly_rate = 20 # $20 per hour
    total_money_made = total_repair_hours * hourly_rate

    # FA
    answer = total_money_made
    return answer