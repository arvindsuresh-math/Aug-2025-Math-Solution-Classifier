def solve():
    """Index: 6783.
    Returns: the number of friends Lyle can treat to a sandwich and juice.
    """
    # L1
    sandwich_cost = 0.30 # A sandwich costs $0.30
    juice_cost = 0.2 # a pack of juice costs $0.2
    total_cost_per_set = sandwich_cost + juice_cost

    # L2
    lyle_money = 2.50 # Lyle has $2.50
    num_sets_lyle_can_buy = lyle_money / total_cost_per_set

    # L3
    lyle_own_set = 1 # the other 1 set is for Lyle himself
    num_friends = num_sets_lyle_can_buy - lyle_own_set

    # FA
    answer = num_friends
    return answer