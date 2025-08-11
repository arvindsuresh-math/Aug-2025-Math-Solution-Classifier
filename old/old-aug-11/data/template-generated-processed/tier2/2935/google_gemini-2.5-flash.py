def solve():
    """Index: 2935.
    Returns: the amount of money Edward has left to buy more toys.
    """
    # L1
    num_toy_cars = 4 # 4 toy cars
    cost_per_toy_car = 0.95 # $0.95 each
    cost_toy_cars = num_toy_cars * cost_per_toy_car

    # L2
    cost_race_track = 6.00 # race track that cost $6.00
    total_cost_toys = cost_toy_cars + cost_race_track

    # L3
    initial_money = 17.80 # Edward had $17.80
    money_left = initial_money - total_cost_toys

    # FA
    answer = money_left
    return answer