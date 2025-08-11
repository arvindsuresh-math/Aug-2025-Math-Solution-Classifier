def solve():
    """Index: 4600.
    Returns: the number of candy bars Nick needs to sell.
    """
    # L1
    chocolate_oranges_sold = 20 # 20 chocolate oranges that he sold out
    chocolate_orange_price = 10 # chocolate oranges for $10
    money_from_oranges = chocolate_oranges_sold * chocolate_orange_price

    # L2
    goal_money = 1000 # raise $1000
    money_needed_from_candy_bars = goal_money - money_from_oranges

    # L3
    candy_bar_price = 5 # candy bars for $5
    candy_bars_to_sell = money_needed_from_candy_bars / candy_bar_price

    # FA
    answer = candy_bars_to_sell
    return answer