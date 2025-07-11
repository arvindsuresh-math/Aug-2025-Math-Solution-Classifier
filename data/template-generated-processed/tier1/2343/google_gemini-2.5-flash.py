def solve():
    """Index: 2343.
    Returns: the number of toy cars Jerome had originally.
    """
    # L1
    cars_last_month = 5 # 5 new toy cars last month
    multiplier_this_month = 2 # twice as many
    cars_this_month = cars_last_month * multiplier_this_month

    # L2
    total_bought = cars_last_month + cars_this_month

    # L3
    total_cars_now = 40 # he has 40 toy cars now
    original_cars = total_cars_now - total_bought

    # FA
    answer = original_cars
    return answer