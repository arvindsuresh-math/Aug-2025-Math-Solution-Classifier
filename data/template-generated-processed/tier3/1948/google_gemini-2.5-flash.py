def solve():
    """Index: 1948.
    Returns: the number of large cups of lemonade Tonya sold.
    """
    # L1
    small_lemonade_sales = 11 # sold $11 worth of small lemonades
    medium_lemonade_sales = 24 # sold $24 worth of medium lemonades
    total_small_medium_sales = small_lemonade_sales + medium_lemonade_sales

    # L2
    total_sales = 50 # ended up making $50
    large_lemonade_sales = total_sales - total_small_medium_sales

    # L3
    price_per_large_cup = 3 # $3 respectively
    num_large_cups_sold = large_lemonade_sales / price_per_large_cup

    # FA
    answer = num_large_cups_sold
    return answer