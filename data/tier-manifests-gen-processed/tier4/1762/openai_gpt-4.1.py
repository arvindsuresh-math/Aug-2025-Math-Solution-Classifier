def solve():
    """Index: 1762.
    Returns: the number of cars that tried to park without paying.
    """
    # L1
    valid_ticket_percent_num = 75 # 75% of the cars have valid tickets
    percent_factor = 0.01 # WK
    total_cars = 300 # 300 cars in the parking lot
    valid_ticket_cars = valid_ticket_percent_num * percent_factor * total_cars

    # L2
    parking_pass_divisor = 5 # 1/5th that number have permanent parking passes
    parking_pass_percent_num = valid_ticket_percent_num / parking_pass_divisor

    # L3
    parking_pass_cars = parking_pass_percent_num * percent_factor * total_cars

    # L4
    illegally_parked_cars = total_cars - valid_ticket_cars - parking_pass_cars

    # FA
    answer = illegally_parked_cars
    return answer