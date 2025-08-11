def solve():
    """Index: 2404.
    Returns: the total number of cars the three of them have altogether.
    """
    # L1
    tommy_cars = 3 # Tommy has 3 toy cars
    jessie_cars = 3 # Jessie, has 3 cars too
    tommy_jessie_combined_cars = tommy_cars + jessie_cars

    # L2
    brother_more_than_combined = 5 # has 5 more cars than Tommy and Jessie
    jessie_brother_cars = brother_more_than_combined + tommy_jessie_combined_cars

    # L3
    total_cars = tommy_jessie_combined_cars + jessie_brother_cars

    # FA
    answer = total_cars
    return answer