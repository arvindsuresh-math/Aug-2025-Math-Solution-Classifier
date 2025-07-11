def solve():
    """Index: 223.
    Returns: the cost of Bob's fruit drink.
    """
    # L1
    num_hamburgers_andy = 2 # two hamburgers
    cost_per_hamburger = 2 # $2 each
    cost_hamburgers_andy = num_hamburgers_andy * cost_per_hamburger

    # L2
    cost_soda_andy = 1 # a can of soda at $1
    total_spent_andy = cost_soda_andy + cost_hamburgers_andy

    # L3
    cost_sandwiches_bob = 3 # two sandwiches for $3
    cost_fruit_drink_bob = total_spent_andy - cost_sandwiches_bob

    # FA
    answer = cost_fruit_drink_bob
    return answer