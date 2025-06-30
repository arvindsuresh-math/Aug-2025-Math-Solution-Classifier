def solve(
    price_large_painting: int = 60, # He charges $60 for a large painting
    price_small_painting: int = 30, # and $30 for a small painting
    num_large_paintings_last_month: int = 8, # Last month he sold eight large paintings
    num_small_paintings_last_month: int = 4, # and four small paintings
    sales_multiplier_this_month: int = 2 # he sold twice as much this month
):
    """Index: 31.
    Returns: Noah's sales for this month.
    """

    #: L1
    sales_large_paintings_last_month = price_large_painting * num_large_paintings_last_month # eval: 480 = 60 * 8

    #: L2
    sales_small_paintings_last_month = price_small_painting * num_small_paintings_last_month # eval: 120 = 30 * 4

    #: L3
    total_sales_last_month = sales_large_paintings_last_month + sales_small_paintings_last_month # eval: 600 = 480 + 120

    #: L4
    total_sales_this_month = total_sales_last_month * sales_multiplier_this_month # eval: 1200 = 600 * 2

    #: FA
    answer = total_sales_this_month # eval: 1200 = 1200
    return answer # eval: return 1200
