def solve():
    """Index: 1848.
    Returns: the total number of bouquets sold during the three day sale.
    """
    # L1
    monday_sales = 12 # On Monday, they sold 12 bouquets
    tuesday_multiplier = 3 # three times that many bouquets
    tuesday_sales = monday_sales * tuesday_multiplier

    # L2
    wednesday_divisor = 3 # a third of what they did the day before
    wednesday_sales = tuesday_sales / wednesday_divisor

    # L3
    total_sales = monday_sales + tuesday_sales + wednesday_sales

    # FA
    answer = total_sales
    return answer