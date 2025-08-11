def solve():
    """Index: 3981.
    Returns: the total number of items James sold.
    """
    # L1
    houses_day1 = 20 # visits 20 houses
    multiplier_twice = 2 # twice as many houses
    houses_day2 = houses_day1 * multiplier_twice

    # L2
    sale_rate_day2 = 0.8 # only sold to 80% of houses
    houses_sold_day2 = houses_day2 * sale_rate_day2

    # L3
    houses_sold_day1 = 20 # manages to sell something in every house
    total_houses_sold = houses_day1 + houses_sold_day2

    # L4
    items_per_house = 2 # sold two things at each house
    total_items_sold = total_houses_sold * items_per_house

    # FA
    answer = total_items_sold
    return answer