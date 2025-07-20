def solve():
    """Index: 5421.
    Returns: the cost of the entree in dollars.
    """
    # L5 (Implicit calculation leading to 2D=18)
    total_spent = 23 # She spends $23 in total
    entree_more_than_dessert = 5 # entree costs $5 more than the dessert
    two_times_dessert_cost = total_spent - entree_more_than_dessert

    # L6
    divisor_for_dessert_cost = 2 # WK
    dessert_cost = two_times_dessert_cost / divisor_for_dessert_cost

    # L7
    entree_cost = dessert_cost + entree_more_than_dessert

    # FA
    answer = entree_cost
    return answer