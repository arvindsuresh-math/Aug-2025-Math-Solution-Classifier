def solve():
    """Index: 6614.
    Returns: the total amount Jake got from selling the snakes.
    """
    # L1
    num_snakes = 3 # Jake has 3 snakes
    eggs_per_snake = 2 # Each of them lays 2 eggs
    total_baby_snakes = num_snakes * eggs_per_snake

    # L2
    rare_snake_count = 1 # one super rare one
    num_regular_snakes = total_baby_snakes - rare_snake_count

    # L3
    price_regular_snake = 250 # sell for $250
    revenue_regular_snakes = num_regular_snakes * price_regular_snake

    # L4
    rare_multiplier = 4 # 4 times as much
    price_rare_snake = price_regular_snake * rare_multiplier

    # L5
    total_revenue = revenue_regular_snakes + price_rare_snake

    # FA
    answer = total_revenue
    return answer