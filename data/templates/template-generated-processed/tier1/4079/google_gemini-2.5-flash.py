def solve():
    """Index: 4079.
    Returns: the amount of money Clare has left.
    """
    # L1
    num_loaves_bread = 4 # 4 loaves of bread
    cost_per_loaf = 2 # Each loaf of bread cost $2
    cost_bread = num_loaves_bread * cost_per_loaf

    # L2
    num_cartons_milk = 2 # 2 cartons of milk
    cost_per_milk_carton = 2 # each carton of milk cost $2
    cost_milk = num_cartons_milk * cost_per_milk_carton

    # L3
    total_groceries_cost = cost_bread + cost_milk

    # L4
    initial_money = 47 # Clare's mother gave her $47
    money_left = initial_money - total_groceries_cost

    # FA
    answer = money_left
    return answer