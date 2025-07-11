def solve():
    """Index: 2404.
    Returns: the total number of cars Tommy, Jessie, and Jessie's brother have altogether.
    """
    # L1
    tommy_cars = 3 # Tommy has 3 toy cars
    jessie_cars = 3 # Jessie has 3 cars too
    tommy_and_jessie_cars = tommy_cars + jessie_cars

    # L2
    brother_more_than_tj = 5 # Jessie's older brother has 5 more cars than Tommy and Jessie
    brother_cars = brother_more_than_tj + tommy_and_jessie_cars

    # L3
    total_cars = tommy_and_jessie_cars + brother_cars

    # FA
    answer = total_cars
    return answer