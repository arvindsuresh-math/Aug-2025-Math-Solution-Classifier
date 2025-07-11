def solve():
    """Index: 6126.
    Returns: the number of pencils in stock at the end of the week.
    """
    # L1
    pencils_per_day = 100 # 100 pencils a day
    days_per_week = 5 # five days a week
    pencils_made = pencils_per_day * days_per_week

    # L2
    initial_stock = 80 # started the week with 80 pencils
    total_available = pencils_made + initial_stock

    # L3
    pencils_sold = 350 # sold 350 pencils
    final_stock = total_available - pencils_sold

    # FA
    answer = final_stock
    return answer