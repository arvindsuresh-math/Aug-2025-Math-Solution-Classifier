def solve():
    """Index: 6126.
    Returns: the number of pencils in stock at the end of the week.
    """
    # L1
    pencils_per_day = 100 # 100 pencils a day
    work_days_per_week = 5 # five days a week
    pencils_made_during_week = pencils_per_day * work_days_per_week

    # L2
    initial_stock = 80 # 80 pencils in his stock
    total_pencils_before_sale = pencils_made_during_week + initial_stock

    # L3
    pencils_sold = 350 # sold 350 pencils
    pencils_at_end_of_week = total_pencils_before_sale - pencils_sold

    # FA
    answer = pencils_at_end_of_week
    return answer