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
    sales_large_last_month = price_large * sold_small_last_month # eval: 240 = 60 * 4

    #: L2
    sales_small_last_month = price_small * sold_small_last_month # eval: 120 = 30 * 4

    #: L3
    total_sales_last_month = sales_large_last_month + sales_small_last_month # eval: 360 = 240 + 120

    #: L4
    total_sales_this_month = total_sales_last_month * multiplier_this_month # eval: 720 = 360 * 2

    #: FA
    answer = total_sales_this_month
    return answer # eval: return 720
