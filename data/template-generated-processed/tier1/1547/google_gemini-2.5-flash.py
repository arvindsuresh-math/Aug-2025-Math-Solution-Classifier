def solve():
    """Index: 1547.
    Returns: the total profit from selling bags of popcorn.
    """
    # L1
    sell_price_per_bag = 8 # sells them for $8
    buy_price_per_bag = 4 # buys bags of popcorn for $4
    profit_per_bag = sell_price_per_bag - buy_price_per_bag

    # L2
    num_bags_sold = 30 # selling 30 bags
    total_profit = num_bags_sold * profit_per_bag

    # FA
    answer = total_profit
    return answer