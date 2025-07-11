def solve():
    """Index: 1015.
    Returns: the amount of money Timmy will have left after buying oranges.
    """
    # L1
    calories_needed = 400 # needs to make sure he gets 400 calories
    calories_per_orange = 80 # Oranges have 80 calories
    oranges_needed = calories_needed / calories_per_orange

    # L2
    cost_per_orange = 1.20 # cost $1.20 each
    total_cost_oranges = oranges_needed * cost_per_orange

    # L3
    initial_money = 10 # Timmy has $10
    money_left = initial_money - total_cost_oranges

    # FA
    answer = money_left
    return answer