def solve():
    """Index: 409.
    Returns: the number of cars Frank needs to sell for the remaining days to meet his quota.
    """
    # L1
    cars_per_day_first_period = 5 # sold 5 cars each day
    cars_sold_first_period = cars_per_day_first_period + cars_per_day_first_period + cars_per_day_first_period

    # L2
    cars_per_day_second_period = 3 # sold 3 cars each day
    cars_sold_second_period = cars_per_day_second_period + cars_per_day_second_period + cars_per_day_second_period + cars_per_day_second_period

    # L3
    total_cars_sold = cars_sold_first_period + cars_sold_second_period

    # L4
    quota_cars = 50 # needs to have 50 cars sold
    cars_left_to_sell = quota_cars - total_cars_sold

    # FA
    answer = cars_left_to_sell
    return answer