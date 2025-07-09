def solve(
    price_large_painting: int = 60, # He charges $60 for a large painting
    price_small_painting: int = 30, # and $30 for a small painting
    num_large_paintings_last_month: int = 8, # Last month he sold eight large paintings
    num_small_paintings_last_month: int = 4, # and four small paintings
    sales_multiplier_this_month: int = 2 # If he sold twice as much this month
):
    """Index: 31.
    Returns: Noah's total sales for this month.
    """

    #: L1

    #: L2
    earnings_small_paintings_last_month = price_small_painting * num_small_paintings_last_month

    #: L3
    total_sales_last_month = sales_multiplier_this_month + earnings_small_paintings_last_month

    #: L4
    total_sales_this_month = total_sales_last_month * sales_multiplier_this_month

    #: FA
    answer = total_sales_this_month
    return answer