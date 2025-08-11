def solve():
    """Index: 4141.
    Returns: the number of chocolate bars James still needs to sell.
    """
    # L1
    sold_last_week = 5 # sold 5 last week
    sold_this_week = 7 # sold 7 this week
    total_sold = sold_last_week + sold_this_week

    # L2
    total_to_sell = 18 # 18 chocolate bars to sell
    needed_to_sell = total_to_sell - total_sold

    # FA
    answer = needed_to_sell
    return answer