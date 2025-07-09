def solve(
        large_painting_price: int = 60, # He charges $60 for a large painting
        small_painting_price: int = 30, # and $30 for a small painting
        large_paintings_sold_last_month: int = 8, # Last month he sold eight large paintings
        small_paintings_sold_last_month: int = 4, # and four small paintings
        sales_multiplier_this_month: int = 2 # If he sold twice as much this month
    ):
    """Index: 31.
    Returns: Noah's total sales for this month.
    """

    #: L1
    earnings_large_paintings_last_month = small_paintings_sold_last_month * large_paintings_sold_last_month

    #: L2
    earnings_small_paintings_last_month = small_painting_price * small_paintings_sold_last_month

    #: L3
    total_sales_last_month = earnings_large_paintings_last_month + earnings_small_paintings_last_month

    #: L4
    sales_this_month = total_sales_last_month * sales_multiplier_this_month

    #: FA
    answer = sales_this_month
    return answer