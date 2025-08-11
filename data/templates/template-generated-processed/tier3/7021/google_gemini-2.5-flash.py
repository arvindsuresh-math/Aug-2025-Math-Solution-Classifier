def solve():
    """Index: 7021.
    Returns: the total number of hours that have passed.
    """
    # L1
    minutes_per_car = 20 # Every 20 minutes
    num_cars = 30 # 30 cars
    total_minutes = minutes_per_car * num_cars

    # L2
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer