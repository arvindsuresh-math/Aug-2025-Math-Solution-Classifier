def solve():
    """Index: 4513.
    Returns: the total profit in dollars after selling 100 apples.
    """
    # L1
    cost_per_bushel = 12 # $12 per bushel
    apples_per_bushel = 48 # 48 apples per bushel
    cost_per_apple_from_farmer = cost_per_bushel / apples_per_bushel

    # L2
    sell_price_per_apple = 0.40 # $0.40 per apple
    profit_per_apple = sell_price_per_apple - cost_per_apple_from_farmer

    # L3
    num_apples_sold = 100 # selling 100 apples
    total_profit = num_apples_sold * profit_per_apple

    # FA
    answer = total_profit
    return answer