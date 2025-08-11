def solve():
    """Index: 1237.
    Returns: the number of cars washed.
    """
    # L1
    num_trucks_washed = 5 # washed 5 trucks
    truck_charge = 6 # $6 for a truck
    earnings_from_trucks = num_trucks_washed * truck_charge

    # L2
    num_suvs_washed = 5 # washed 5 SUVs
    suv_charge = 7 # $7 for an SUV
    earnings_from_suvs = num_suvs_washed * suv_charge

    # L3
    total_raised = 100 # raised $100 in total
    earnings_from_cars = total_raised - earnings_from_suvs - earnings_from_trucks

    # L4
    car_charge = 5 # $5 for a car
    num_cars_washed = earnings_from_cars / car_charge

    # FA
    answer = num_cars_washed
    return answer