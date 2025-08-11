def solve():
    """Index: 1547.
    Returns: the total profit John makes by selling 30 bags of popcorn.
    """
    # L1
    sell_price = 8 # sells them for $8
    buy_price = 4 # buys bags of popcorn for $4
    profit_per_bag = sell_price - buy_price

    # L2
    num_bags = 30 # selling 30 bags
    total_profit = num_bags * profit_per_bag

    # FA
    answer = total_profit
    return answer