def solve():
    """Index: 6196.
    Returns: the number of small orders Lisa has sent.
    """
    # L1
    num_large_orders = 3 # she knows she has sent 3 large orders
    peanuts_per_large_order = 200 # Each large order needs 200g of packing peanuts
    peanuts_used_large_orders = num_large_orders * peanuts_per_large_order

    # L2
    total_peanuts_used = 800 # If Lisa has used a total of 800g of packing peanuts
    peanuts_used_small_orders = total_peanuts_used - peanuts_used_large_orders

    # L3
    peanuts_per_small_order = 50 # small orders need just 50g of packing peanuts
    num_small_orders = peanuts_used_small_orders / peanuts_per_small_order

    # FA
    answer = num_small_orders
    return answer