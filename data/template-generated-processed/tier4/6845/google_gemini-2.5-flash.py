def solve():
    """Index: 6845.
    Returns: the total profit from selling apples and oranges.
    """
    # L1
    apple_buy_cost_num = 3 # bought apples at 2 for $3
    apple_buy_quantity = 2 # bought apples at 2 for $3
    apple_cost_per_unit = apple_buy_cost_num / apple_buy_quantity

    # L2
    apple_sell_cost_num = 10 # sell them at 5 for $10
    apple_sell_quantity = 5 # sell them at 5 for $10
    apple_sell_price_per_unit = apple_sell_cost_num / apple_sell_quantity

    # L3
    apple_profit_per_unit = apple_sell_price_per_unit - apple_cost_per_unit

    # L4
    num_apples_sold = 5 # sells 5 apples
    total_apple_profit = apple_profit_per_unit * num_apples_sold

    # L5
    orange_buy_cost_num = 2.70 # bought 3 oranges for $2.70
    orange_buy_quantity = 3 # bought 3 oranges for $2.70
    orange_cost_per_unit = orange_buy_cost_num / orange_buy_quantity

    # L6
    orange_sell_price_per_unit = 1 # sell them at $1 each
    orange_profit_per_unit = orange_sell_price_per_unit - orange_cost_per_unit

    # L7
    num_oranges_sold = 5 # sells 5 oranges
    total_orange_profit = orange_profit_per_unit * num_oranges_sold

    # L8
    total_profit = total_apple_profit + total_orange_profit

    # FA
    answer = total_profit
    return answer