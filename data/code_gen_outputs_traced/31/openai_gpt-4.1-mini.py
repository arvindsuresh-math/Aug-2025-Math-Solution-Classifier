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
    sales_large_last_month = price_large * sold_large_last_month # eval: 480 = 60 * 8
    #: L2
    sales_small_last_month = price_small * sold_small_last_month # eval: 120 = 30 * 4
    #: L3
    total_sales_last_month = sales_large_last_month + sales_small_last_month # eval: 600 = 480 + 120
    #: L4
    total_sales_this_month = total_sales_last_month * multiplier_this_month # eval: 1200 = 600 * 2
    answer = total_sales_this_month  # FINAL ANSWER # eval: 1200 = 1200  # FINAL ANSWER
    return answer # eval: return 1200