def solve():
    """Index: 3465.
    Returns: the amount of money Wyatt has left.
    """
    # L1
    num_loaves_bread = 5 # 5 loaves of bread
    cost_per_loaf = 5 # Each loaf of bread cost $5
    cost_bread = num_loaves_bread * cost_per_loaf

    # L2
    num_cartons_oj = 4 # 4 cartons of orange juice
    cost_per_carton_oj = 2 # each carton of orange juice cost $2
    cost_orange_juice = num_cartons_oj * cost_per_carton_oj

    # L3
    total_cost = cost_bread + cost_orange_juice

    # L4
    initial_money = 74 # $74 to go to the store
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer