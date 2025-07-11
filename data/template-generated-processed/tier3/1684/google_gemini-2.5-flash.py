def solve():
    """Index: 1684.
    Returns: the number of chips sold in the third and fourth week, respectively.
    """
    # L1
    initial_sales_week1 = 15 # In the first week, 15 bags of chips were sold
    multiplier = 3 # thrice as many bags of chips
    sales_week2 = initial_sales_week1 * multiplier

    # L2
    total_sales_week1_2 = sales_week2 + initial_sales_week1

    # L3
    total_sales_month = 100 # sold 100 bags of chips in a month
    remaining_sales_week3_4 = total_sales_month - total_sales_week1_2

    # L4
    num_weeks_equal_sales = 2 # equal number of chips sold in the third and fourth week
    sales_per_week_3_4 = remaining_sales_week3_4 / num_weeks_equal_sales

    # FA
    answer = sales_per_week_3_4
    return answer