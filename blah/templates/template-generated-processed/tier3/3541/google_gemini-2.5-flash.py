def solve():
    """Index: 3541.
    Returns: the number of customers in each car.
    """
    # L1
    sports_store_sales = 20 # the sports store makes 20 sales
    music_store_sales = 30 # the music store makes 30 sales
    total_customers = sports_store_sales + music_store_sales

    # L2
    num_cars = 10 # 10 cars parked
    customers_per_car = total_customers / num_cars

    # FA
    answer = customers_per_car
    return answer