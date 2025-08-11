def solve():
    """Index: 4036.
    Returns: the number of cakes Marjorie made on the first day.
    """
    # L1
    cakes_on_sixth_day = 320 # On the sixth day, she makes 320 cakes
    doubling_factor = 2 # twice as many cakes as she did the day before
    cakes_on_fifth_day = cakes_on_sixth_day / doubling_factor

    # L2
    cakes_on_fourth_day = cakes_on_fifth_day / doubling_factor

    # L3
    cakes_on_third_day = cakes_on_fourth_day / doubling_factor

    # L4
    cakes_on_second_day = cakes_on_third_day / doubling_factor

    # L5
    cakes_on_first_day = cakes_on_second_day / doubling_factor

    # FA
    answer = cakes_on_first_day
    return answer