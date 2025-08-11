def solve():
    """Index: 100.
    Returns: the number of sales in the stationery section.
    """
    # L1
    total_sales = 36 # They made 36 sales today
    fabric_denominator = 3 # a third of its sales
    fabric_sales = total_sales / fabric_denominator

    # L2
    jewelry_denominator = 4 # a quarter of its sales
    jewelry_sales = total_sales / jewelry_denominator

    # L3
    stationery_sales = total_sales - fabric_sales - jewelry_sales

    # FA
    answer = stationery_sales
    return answer