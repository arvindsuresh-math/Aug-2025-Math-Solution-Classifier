def solve():
    """Index: 2420.
    Returns: the final cost per pineapple.
    """
    # L1
    num_pineapples = 12 # they buy a dozen
    cost_per_pineapple_initial = 1.25 # Each pineapple costs $1.25
    total_pineapple_cost = num_pineapples * cost_per_pineapple_initial

    # L2
    shipping_cost = 21.00 # It will cost $21.00 to ship all of them
    total_cost = total_pineapple_cost + shipping_cost

    # L3
    cost_per_pineapple_final = total_cost / num_pineapples

    # FA
    answer = cost_per_pineapple_final
    return answer