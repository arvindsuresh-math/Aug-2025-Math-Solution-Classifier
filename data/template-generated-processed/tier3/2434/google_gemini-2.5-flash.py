def solve():
    """Index: 2434.
    Returns: the total number of boxes sold over the three days.
    """
    # L1
    friday_sales = 40 # On Friday, she sold 40 boxes
    twice_multiplier = 2 # twice that number
    fewer_amount = 10 # 10 fewer
    saturday_sales = twice_multiplier * friday_sales - fewer_amount

    # L2
    half_divisor = 2 # half as many as Sunday (interpreted as half of Saturday's sales based on solution)
    sunday_sales = saturday_sales / half_divisor

    # L3
    total_sales = friday_sales + saturday_sales + sunday_sales

    # FA
    answer = total_sales
    return answer