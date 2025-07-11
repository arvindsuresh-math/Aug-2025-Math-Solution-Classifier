def solve():
    """Index: 731.
    Returns: the total earnings of the clothing store if all shirts and jeans are sold.
    """
    # L1
    shirt_cost = 10 # A shirt costs $10 each
    num_shirts = 20 # sells 20 shirts
    total_shirt_revenue = shirt_cost * num_shirts

    # L2
    jeans_cost_multiplier = 2 # a pair of jeans costs twice as much
    jeans_cost_per_pair = shirt_cost * jeans_cost_multiplier

    # L3
    num_jeans_pairs = 10 # 10 pairs of jeans
    total_jeans_revenue = jeans_cost_per_pair * num_jeans_pairs

    # L4
    total_revenue = total_shirt_revenue + total_jeans_revenue

    # FA
    answer = total_revenue
    return answer