def solve():
    """Index: 4404.
    Returns: the profit John makes.
    """
    # L1
    num_woodburning_sold = 20 # 20 woodburning
    price_per_woodburning = 15 # $15 each
    total_sales = num_woodburning_sold * price_per_woodburning

    # L2
    wood_cost = 100 # The wood cost $100
    profit = total_sales - wood_cost

    # FA
    answer = profit
    return answer