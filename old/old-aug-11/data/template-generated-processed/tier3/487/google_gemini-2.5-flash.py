def solve():
    """Index: 487.
    Returns: the profit Jonah made.
    """
    # L1
    num_pineapples = 6 # Jonah bought 6 pineapples
    cost_per_pineapple = 3 # for $3 each
    total_spent = num_pineapples * cost_per_pineapple

    # L2
    rings_per_pineapple = 12 # Each pineapple could be cut into 12 pineapple rings
    total_pineapple_rings = num_pineapples * rings_per_pineapple

    # L3
    rings_per_set_sold = 4 # sold 4 pineapple rings
    num_sets_sold = total_pineapple_rings / rings_per_set_sold

    # L4
    price_per_set = 5 # for $5 each
    total_revenue = num_sets_sold * price_per_set

    # L5
    profit = total_revenue - total_spent

    # FA
    answer = profit
    return answer