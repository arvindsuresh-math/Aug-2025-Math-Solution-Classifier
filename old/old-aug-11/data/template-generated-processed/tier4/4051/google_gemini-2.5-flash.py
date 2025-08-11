def solve():
    """Index: 4051.
    Returns: the amount each friend will pay if they split the bill equally.
    """
    # L1
    hamburger_cost_per_item = 5 # $5 each
    num_hamburgers = 5 # 5 orders of Dave's Single hamburger
    total_hamburger_cost = hamburger_cost_per_item * num_hamburgers

    # L2
    fries_cost_per_set = 2.50 # $2.50
    num_fries_sets = 4 # 4 sets of french fries
    total_fries_cost = fries_cost_per_set * num_fries_sets

    # L3
    lemonade_cost_per_cup = 2 # $2 each
    num_lemonade_cups = 5 # 5 cups of peach lemonade
    total_lemonade_cost = lemonade_cost_per_cup * num_lemonade_cups

    # L4
    taco_salad_cost = 10 # a platter of Taco Salad that cost $10
    total_bill = taco_salad_cost + total_hamburger_cost + total_fries_cost + total_lemonade_cost

    # L5
    num_friends = 5 # Five friends
    cost_per_friend = total_bill / num_friends

    # FA
    answer = cost_per_friend
    return answer