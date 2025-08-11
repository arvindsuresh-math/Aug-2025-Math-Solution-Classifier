def solve():
    """Index: 7378.
    Returns: the total number of ice cream cones sold.
    """
    # L1
    tuesday_sales = 12000 # 12,000 ice cream cones were sold
    double_multiplier = 2 # double the amount
    wednesday_sales = tuesday_sales * double_multiplier

    # L2
    total_sales = tuesday_sales + wednesday_sales

    # FA
    answer = total_sales
    return answer