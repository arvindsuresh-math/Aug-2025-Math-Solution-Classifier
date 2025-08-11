def solve():
    """Index: 4315.
    Returns: the total money Farmer Kent would make from selling watermelons.
    """
    # L1
    price_per_pound = 2 # for $2 a pound
    watermelon_weight = 23 # weighs 23 pounds
    price_per_watermelon = price_per_pound * watermelon_weight

    # L2
    num_watermelons_sold = 18 # selling 18 watermelons
    total_money = price_per_watermelon * num_watermelons_sold

    # FA
    answer = total_money
    return answer