def solve():
    """Index: 5990.
    Returns: the number of years it will take to reduce the car collection.
    """
    # L1
    initial_cars = 3500 # Oprah has 3500 cars in her collection
    target_cars = 500 # reduce her car collection to 500
    cars_to_give_away = initial_cars - target_cars

    # L2
    cars_per_year = 50 # average number of cars she gives away per year is 50
    years_needed = cars_to_give_away / cars_per_year

    # FA
    answer = years_needed
    return answer