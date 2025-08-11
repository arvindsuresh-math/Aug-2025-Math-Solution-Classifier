def solve():
    """Index: 3704.
    Returns: the number of televisions sold on Black Friday three years from now.
    """
    # L1
    current_year_sales = 327 # 327 televisions
    increase_per_year = 50 # 50 more televisions each year
    sales_year_1 = current_year_sales + increase_per_year

    # L2
    sales_year_2 = sales_year_1 + increase_per_year

    # L3
    sales_year_3 = sales_year_2 + increase_per_year

    # FA
    answer = sales_year_3
    return answer