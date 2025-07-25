def solve():
    """Index: 5989.
    Returns: the amount of money Sarah started with.
    """
    # L1
    money_remaining_after_beanie = 7 # If she has $7 remaining after purchasing the beanie
    cost_beanie = 14 # a beanie for $14 for her brother
    money_before_beanie = money_remaining_after_beanie + cost_beanie

    # L2
    cost_scarf = 10 # a scarf for $10 for her mother
    money_before_scarf = money_before_beanie + cost_scarf

    # L3
    num_toy_cars = 2 # 2 toy cars
    cost_per_toy_car = 11 # $11 each for her sons
    total_cost_toy_cars = num_toy_cars * cost_per_toy_car

    # L4
    initial_money = money_before_scarf + total_cost_toy_cars

    # FA
    answer = initial_money
    return answer