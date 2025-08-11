def solve():
    """Index: 2499.
    Returns: the number of loaves of bread at the end of the day.
    """
    # L1
    initial_loaves = 2355 # 2355 loaves of bread at the start of the day
    sold_loaves = 629 # 629 loaves are sold
    loaves_after_sales = initial_loaves - sold_loaves

    # L2
    delivered_loaves = 489 # 489 loaves are delivered to the supermarket
    loaves_end_of_day = loaves_after_sales + delivered_loaves

    # FA
    answer = loaves_end_of_day
    return answer