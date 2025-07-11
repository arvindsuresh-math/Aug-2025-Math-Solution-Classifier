def solve():
    """Index: 129.
    Returns: the number of free ice cream cones Dan gave away.
    """
    # L1
    total_sales = 100 # sold $100 worth of cones
    cone_price = 2 # Cones cost $2 each
    cones_sold = total_sales / cone_price

    # L2
    paying_customers_per_free = 5 # every sixth customer gets a free cone (so 5 pay, 1 free)
    free_cones = cones_sold / paying_customers_per_free

    # FA
    answer = free_cones
    return answer