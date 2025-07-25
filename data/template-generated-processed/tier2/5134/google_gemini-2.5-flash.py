def solve():
    """Index: 5134.
    Returns: the total number of cars counted by all of them.
    """
    # L1
    jared_cars = 300 # Jared counted 300 cars
    ann_increase_factor_decimal = 1.15 # WK
    ann_cars = ann_increase_factor_decimal * jared_cars

    # L2
    cars_more_than_alfred = 7 # Ann counted 7 more cars than their friend Alfred
    alfred_cars = ann_cars - cars_more_than_alfred

    # L3
    total_cars = alfred_cars + ann_cars + jared_cars

    # FA
    answer = total_cars
    return answer