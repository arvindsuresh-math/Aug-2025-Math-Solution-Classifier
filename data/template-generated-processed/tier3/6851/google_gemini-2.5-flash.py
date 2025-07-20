def solve():
    """Index: 6851.
    Returns: the number of large glasses Peter bought.
    """
    # L1
    total_money_had = 50 # He has $50
    change_left = 1 # leaves with $1 in change
    money_spent_on_glasses = total_money_had - change_left

    # L2
    num_small_glasses = 8 # buys 8 small ones
    cost_small_glass = 3 # cost $3 for small glasses
    cost_of_small_glasses = num_small_glasses * cost_small_glass

    # L3
    cost_of_large_glasses = money_spent_on_glasses - cost_of_small_glasses

    # L4
    cost_large_glass = 5 # $5 for large ones
    num_large_glasses = cost_of_large_glasses / cost_large_glass

    # FA
    answer = num_large_glasses
    return answer