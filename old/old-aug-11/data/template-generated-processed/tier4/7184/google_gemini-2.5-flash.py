def solve():
    """Index: 7184.
    Returns: the cost of each pair of sunglasses to the vendor.
    """
    # L1
    sign_cost = 20 # costs $20
    profit_fraction_for_sign = 0.5 # half his profits
    total_profits = sign_cost / profit_fraction_for_sign

    # L2
    pairs_sold = 10 # sells 10 pairs
    selling_price_per_pair = 30 # selling sunglasses for $30 each
    total_revenue = pairs_sold * selling_price_per_pair

    # L3
    total_cost = total_revenue - total_profits

    # L4
    cost_per_pair = total_cost / pairs_sold

    # FA
    answer = cost_per_pair
    return answer