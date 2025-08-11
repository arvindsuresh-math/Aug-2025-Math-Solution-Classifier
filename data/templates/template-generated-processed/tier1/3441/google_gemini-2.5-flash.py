def solve():
    """Index: 3441.
    Returns: the profit of the pet store.
    """
    # L1
    brandon_sold_price = 100 # Brandon sold the geckos for 100$
    more_than_multiplier = 5 # 5 more
    times_multiplier = 3 # 3 times that
    pet_store_sell_price = more_than_multiplier + times_multiplier * brandon_sold_price

    # L2
    pet_store_profit = pet_store_sell_price - brandon_sold_price

    # FA
    answer = pet_store_profit
    return answer