def solve(
    price_large: int = 60,  # $60 for a large painting
    price_small: int = 30,  # $30 for a small painting
    sold_large_last_month: int = 8,  # sold eight large paintings last month
    sold_small_last_month: int = 4,  # sold four small paintings last month
    multiplier_this_month: int = 2  # sold twice as much this month
):
    """Index: 31.
    Returns: the total sales amount for this month.
    """

    #: L1
    sales_large_last_month = price_large * sold_large_last_month

    #: L2
    sales_small_last_month = price_small * sold_small_last_month

    #: L3
    total_sales_last_month = sales_large_last_month + sales_small_last_month

    #: L4
    total_sales_this_month = total_sales_last_month * multiplier_this_month

    #: FA
    answer = total_sales_this_month
    return answer