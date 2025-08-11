def solve():
    """Index: 2054.
    Returns: the total number of copies of the book sold by Friday.
    """
    # L1
    wednesday_sales = 15 # sold 15 copies at the bookstore on Wednesday
    thursday_multiplier = 3 # three times that many copies
    thursday_sales = wednesday_sales * thursday_multiplier

    # L2
    friday_divisor = 5 # one-fifth the number of copies
    friday_sales = thursday_sales / friday_divisor

    # L3
    total_sales_by_friday = wednesday_sales + thursday_sales + friday_sales

    # FA
    answer = total_sales_by_friday
    return answer