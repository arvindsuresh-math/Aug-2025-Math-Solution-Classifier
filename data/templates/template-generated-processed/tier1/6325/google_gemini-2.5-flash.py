def solve():
    """Index: 6325.
    Returns: the money Rihanna has left.
    """
    # L1
    num_mangoes = 6 # 6 mangoes
    cost_per_mango = 3 # Each mango cost $3
    cost_mangoes = num_mangoes * cost_per_mango

    # L2
    num_apple_juice_cartons = 6 # 6 cartons of apple juice
    cost_per_apple_juice_carton = 3 # each carton of apple juice cost $3
    cost_apple_juice = num_apple_juice_cartons * cost_per_apple_juice_carton

    # L3
    total_cost = cost_mangoes + cost_apple_juice

    # L4
    initial_money = 50 # $50 to go to the supermarket
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer