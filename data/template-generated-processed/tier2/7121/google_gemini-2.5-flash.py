def solve():
    """Index: 7121.
    Returns: the amount Jenny makes after factoring in expenses.
    """
    # L1
    cost_per_pan = 10.00 # It costs Jenny $10.00 in ingredients to make 1 pan of lasagna.
    num_pans = 20 # sells 20 pans
    total_ingredient_cost = cost_per_pan * num_pans

    # L2
    sale_price_per_pan = 25.00 # at $25.00 apiece
    total_revenue = num_pans * sale_price_per_pan

    # L3
    net_profit = total_revenue - total_ingredient_cost

    # FA
    answer = net_profit
    return answer