def solve():
    """Index: 1351.
    Returns: the difference in stuffed animals sold between Quincy and Jake.
    """
    # L1
    quincy_sold_total = 200 # Quincy sold 200 stuffed animals
    quincy_multiplier = 10 # ten times as many stuffed animals as Thor
    thor_sold = quincy_sold_total / quincy_multiplier

    # L2
    jake_more_than_thor = 10 # 10 more stuffed animals than Thor
    jake_sold = thor_sold + jake_more_than_thor

    # L3
    difference_quincy_jake = quincy_sold_total - jake_sold

    # FA
    answer = difference_quincy_jake
    return answer