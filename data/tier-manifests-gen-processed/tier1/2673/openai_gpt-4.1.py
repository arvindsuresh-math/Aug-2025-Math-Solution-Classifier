def solve():
    """Index: 2673.
    Returns: the total amount Alice had saved by the end of the third month.
    """
    # L2
    first_month_saved = 10 # saved 10 dollars the first month
    monthly_increase = 30 # 30 more each month
    second_month_saved = first_month_saved + monthly_increase

    # L3
    third_month_saved = second_month_saved + monthly_increase

    # FA
    answer = third_month_saved
    return answer