def solve():
    """Index: 1966.
    Returns: the number of shirts Selina sold to the store.
    """
    # L1
    shirts_bought_count = 2 # 2 shirts that she likes
    cost_per_bought_shirt = 10 # cost $10 each
    cost_of_bought_shirts = shirts_bought_count * cost_per_bought_shirt

    # L2
    money_left_store = 30 # She leaves the store with $30
    total_money_earned = cost_of_bought_shirts + money_left_store

    # L3
    pants_sold_count = 3 # sells 3 pairs of pants
    price_per_pant = 5 # pants for $5 each
    money_from_pants = pants_sold_count * price_per_pant

    # L4
    shorts_sold_count = 5 # 5 pairs of shorts
    price_per_short = 3 # shorts for $3 each
    money_from_shorts = price_per_short * shorts_sold_count

    # L5
    money_from_shirts = total_money_earned - money_from_pants - money_from_shorts

    # L6
    price_per_sold_shirt = 4 # shirts for $4 each
    shirts_sold_count = money_from_shirts / price_per_sold_shirt

    # FA
    answer = shirts_sold_count
    return answer