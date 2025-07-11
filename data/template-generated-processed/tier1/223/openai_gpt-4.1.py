def solve():
    """Index: 223.
    Returns: the cost of Bob's fruit drink.
    """
    # L1
    num_hamburgers = 2 # two hamburgers
    price_per_hamburger = 2 # $2 each
    total_hamburger_cost = num_hamburgers * price_per_hamburger

    # L2
    andy_soda_cost = 1 # a can of soda at $1
    andy_total = andy_soda_cost + total_hamburger_cost

    # L3
    bob_sandwiches_cost = 3 # two sandwiches for $3
    bob_fruit_drink_cost = andy_total - bob_sandwiches_cost

    # FA
    answer = bob_fruit_drink_cost
    return answer