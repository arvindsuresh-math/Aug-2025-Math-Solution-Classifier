def solve(
        large_painting_price: int = 60,  # He charges $60 for a large painting
        small_painting_price: int = 30,  # He charges $30 for a small painting
        large_paintings_last_month: int = 8,  # Last month he sold eight large paintings
        small_paintings_last_month: int = 4  # Last month he sold four small paintings
):
    """Index: 31.
    Returns: Noah's total sales for this month.
    """

    #: L1
    large_painting_revenue = large_painting_price * large_paintings_last_month # eval: 480 = 60 * 8

    #: L2
    small_painting_revenue = small_painting_price * small_paintings_last_month # eval: 120 = 30 * 4

    #: L3
    total_sales_last_month = large_painting_revenue + small_painting_revenue # eval: 600 = 480 + 120

    #: L4
    total_sales_this_month = total_sales_last_month * 2 # eval: 1200 = 600 * 2

    #: FA
    answer = total_sales_this_month # eval: 1200 = 1200
    return answer # eval: return 1200
