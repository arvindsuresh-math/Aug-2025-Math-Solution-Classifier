def solve():
    """Index: 409.
    Returns: the number of cars Frank needs to sell in the remaining days to meet his quota.
    """
    # L1
    days_5cars = 3 # first three days
    cars_per_day_5 = 5 # 5 cars each day
    cars_5days = cars_per_day_5 + cars_per_day_5 + cars_per_day_5

    # L2
    days_3cars = 4 # next 4 days
    cars_per_day_3 = 3 # 3 cars each day
    cars_3days = cars_per_day_3 + cars_per_day_3 + cars_per_day_3 + cars_per_day_3

    # L3
    total_sold = cars_5days + cars_3days

    # L4
    quota = 50 # needs to have 50 cars sold
    cars_left = quota - total_sold

    # FA
    answer = cars_left
    return answer