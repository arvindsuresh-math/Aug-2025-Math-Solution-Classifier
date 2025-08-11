def solve():
    """Index: 6810.
    Returns: the number of cakes left with Brenda.
    """
    # L1
    cakes_per_day = 20 # bakes 20 cakes a day
    number_of_days = 9 # for 9 days
    total_cakes_baked = cakes_per_day * number_of_days

    # L2
    cakes_sold_divisor = 2 # sells half of the cakes
    cakes_remaining = total_cakes_baked / cakes_sold_divisor

    # FA
    answer = cakes_remaining
    return answer