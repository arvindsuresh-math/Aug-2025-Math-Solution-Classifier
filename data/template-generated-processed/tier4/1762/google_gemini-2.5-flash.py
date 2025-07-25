def solve():
    """Index: 1762.
    Returns: the number of people who tried to park without paying.
    """
    # L1
    total_cars = 300 # 300 cars in the parking lot
    valid_tickets_percent_num = 75 # 75% of the cars have valid tickets
    percent_factor = 0.01 # WK
    cars_with_valid_tickets = valid_tickets_percent_num * percent_factor * total_cars

    # L2
    parking_pass_divisor = 5 # 1/5th that number have permanent parking passes
    parking_pass_percent_num = valid_tickets_percent_num / parking_pass_divisor

    # L3
    cars_with_parking_passes = parking_pass_percent_num * percent_factor * total_cars

    # L4
    cars_parked_illegally = total_cars - cars_with_valid_tickets - cars_with_parking_passes

    # FA
    answer = cars_parked_illegally
    return answer