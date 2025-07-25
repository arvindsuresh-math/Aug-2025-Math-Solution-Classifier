def solve():
    """Index: 31.
    Returns: Noah's total sales for this month.
    """
    # L1
    price_large = 60 # charges $60 for a large painting
    num_large_last_month = 8 # sold eight large paintings
    large_sales_last_month = price_large * num_large_last_month

    # L2
    price_small = 30 # charges $30 for a small painting
    num_small_last_month = 4 # sold four small paintings
    small_sales_last_month = price_small * num_small_last_month

    # L3
    total_sales_last_month = large_sales_last_month + small_sales_last_month

    # L4
    sales_multiplier = 2 # sold twice as much this month
    total_sales_this_month = total_sales_last_month * sales_multiplier

    # FA
    answer = total_sales_this_month
    return answer