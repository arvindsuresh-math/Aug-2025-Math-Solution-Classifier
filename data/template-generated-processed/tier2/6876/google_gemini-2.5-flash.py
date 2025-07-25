def solve():
    """Index: 6876.
    Returns: the amount of money Selena will be left with.
    """
    # L1
    steak_cost_per_plate = 24 # 2 steak meals that cost $24 each plate
    num_steak_meals = 2 # 2 steak meals
    steaks_total_cost = steak_cost_per_plate * num_steak_meals

    # L2
    burger_cost_per_type = 3.5 # burgers which cost $3.5 each
    num_burger_types = 2 # 2 types of burgers
    burgers_total_cost = burger_cost_per_type * num_burger_types

    # L3
    ice_cream_cost_per_cup = 2 # ice cream which cost $2 each
    num_ice_cream_cups = 3 # 3 cups of ice cream
    ice_cream_total_cost = ice_cream_cost_per_cup * num_ice_cream_cups

    # L4
    total_charged_food = steaks_total_cost + burgers_total_cost + ice_cream_total_cost

    # L5
    initial_tip_amount = 99 # tip today that amounted to $99
    money_left = initial_tip_amount - total_charged_food

    # FA
    answer = money_left
    return answer