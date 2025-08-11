def solve():
    """Index: 5854.
    Returns: the total amount of money in dollars.
    """
    # L1
    gold_coin_value = 50 # 50 dollars
    num_gold_coins = 3 # 3 gold coins
    total_gold_value = gold_coin_value * num_gold_coins

    # L2
    silver_coin_value = 25 # 25 dollars
    num_silver_coins = 5 # 5 silver coins
    total_silver_value = silver_coin_value * num_silver_coins

    # L3
    cash_amount = 30 # 30 dollars cash
    total_money = cash_amount + total_silver_value + total_gold_value

    # FA
    answer = total_money
    return answer