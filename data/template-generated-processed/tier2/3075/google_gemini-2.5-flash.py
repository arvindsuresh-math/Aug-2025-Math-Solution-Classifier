def solve():
    """Index: 3075.
    Returns: the total profit James makes from the sales.
    """
    # L1
    selling_price_per_bar = 1.5 # sells each candy bar for $1.50
    buying_price_per_bar = 1 # buys each bar for $1
    profit_per_bar = selling_price_per_bar - buying_price_per_bar

    # L2
    num_boxes_sold = 5 # sells 5 boxes
    candy_bars_per_box = 10 # Each box has 10 candy bars
    total_candy_bars_sold = num_boxes_sold * candy_bars_per_box

    # L3
    total_profit = total_candy_bars_sold * profit_per_bar

    # FA
    answer = total_profit
    return answer