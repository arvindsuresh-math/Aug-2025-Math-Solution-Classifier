def solve():
    """Index: 2420.
    Returns: the total cost per pineapple including shipping.
    """
    # L1
    num_pineapples = 12 # a dozen
    pineapple_price = 1.25 # Each pineapple costs $1.25
    total_pineapple_cost = num_pineapples * pineapple_price

    # L2
    shipping_cost = 21.00 # it will cost $21.00 to ship all of them
    total_cost = total_pineapple_cost + shipping_cost

    # L3
    cost_per_pineapple = total_cost / num_pineapples

    # FA
    answer = cost_per_pineapple
    return answer