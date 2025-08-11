def solve():
    """Index: 6279.
    Returns: the total money Michael made this week.
    """
    # L1
    num_large_birdhouses_sold = 2 # sold 2 large birdhouses
    price_large_birdhouse = 22 # charges $22 for each large birdhouse
    large_birdhouse_sales = num_large_birdhouses_sold * price_large_birdhouse

    # L2
    num_medium_birdhouses_sold = 2 # sold 2 medium birdhouses
    price_medium_birdhouse = 16 # charges $16 for each medium birdhouse
    medium_birdhouse_sales = num_medium_birdhouses_sold * price_medium_birdhouse

    # L3
    num_small_birdhouses_sold = 3 # sold 3 small birdhouses
    price_small_birdhouse = 7 # charges $7 for each small birdhouse
    small_birdhouse_sales = num_small_birdhouses_sold * price_small_birdhouse

    # L4
    total_money_made = large_birdhouse_sales + medium_birdhouse_sales + small_birdhouse_sales

    # FA
    answer = total_money_made
    return answer