def solve():
    """Index: 2935.
    Returns: the amount of money Edward has left to buy more toys.
    """
    # L1
    num_toy_cars = 4 # 4 toy cars
    toy_car_cost = 0.95 # cost $0.95 each
    toy_cars_total = num_toy_cars * toy_car_cost

    # L2
    race_track_cost = 6.00 # race track that cost $6.00
    total_toys_cost = toy_cars_total + race_track_cost

    # L3
    initial_money = 17.80 # Edward had $17.80
    money_left = initial_money - total_toys_cost

    # FA
    answer = money_left
    return answer