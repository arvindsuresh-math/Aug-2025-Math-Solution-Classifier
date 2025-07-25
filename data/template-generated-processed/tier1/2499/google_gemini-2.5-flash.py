def solve():
    """Index: 2499.
    Returns: the number of loaves of bread at the end of the day.
    """
    # L1
    initial_loaves = 2355 # 2355 loaves of bread at the start of the day
    loaves_sold = 629 # 629 loaves are sold
    loaves_after_sale = initial_loaves - loaves_sold

    # L2
    loaves_delivered = 489 # 489 loaves are delivered
    final_loaves = loaves_after_sale + loaves_delivered

    # FA
    answer = final_loaves
    return answer