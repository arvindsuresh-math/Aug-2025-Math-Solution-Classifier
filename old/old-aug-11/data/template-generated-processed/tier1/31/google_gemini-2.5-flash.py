def solve():
    """Index: 31.
    Returns: Noah's total sales for this month.
    """
    # L1
    price_large_painting = 60 # charges $60 for a large painting
    num_large_paintings_last_month = 8 # sold eight large paintings
    sales_large_paintings_last_month = price_large_painting * num_large_paintings_last_month

    # L2
    price_small_painting = 30 # charges $30 for a small painting
    num_small_paintings_last_month = 4 # sold four small paintings
    sales_small_paintings_last_month = price_small_painting * num_small_paintings_last_month

    # L3
    total_sales_last_month = sales_large_paintings_last_month + sales_small_paintings_last_month

    # L4
    multiplier_this_month = 2 # sold twice as much this month
    sales_this_month = total_sales_last_month * multiplier_this_month

    # FA
    answer = sales_this_month
    return answer