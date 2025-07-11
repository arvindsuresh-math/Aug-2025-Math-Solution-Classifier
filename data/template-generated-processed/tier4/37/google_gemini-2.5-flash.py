def solve():
    """Index: 37.
    Returns: the amount each friend will pay if they split the bill equally.
    """
    # L1
    hamburger_price_per_piece = 3 # $3 each
    num_hamburgers = 5 # 5 pieces of hamburger
    cost_hamburgers = hamburger_price_per_piece * num_hamburgers

    # L2
    fries_price_per_set = 1.20 # $1.20
    num_fries_sets = 4 # 4 sets of French fries
    cost_fries = fries_price_per_set * num_fries_sets

    # L3
    soda_price_per_cup = 0.5 # $0.5 each
    num_soda_cups = 5 # 5 cups of soda
    cost_soda = soda_price_per_cup * num_soda_cups

    # L4
    spaghetti_cost = 2.7 # 1 platter of spaghetti that cost $2.7
    total_bill = cost_hamburgers + cost_fries + cost_soda + spaghetti_cost

    # L5
    num_friends = 5 # Five friends
    cost_per_friend = total_bill / num_friends

    # FA
    answer = cost_per_friend
    return answer