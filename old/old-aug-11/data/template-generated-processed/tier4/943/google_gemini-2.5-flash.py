def solve():
    """Index: 943.
    Returns: the number of dozen donuts Javier needs to buy and sell.
    """
    # L1
    cost_per_dozen_donuts = 2.40 # He buys each dozen donuts for $2.40
    donuts_per_dozen = 12 # WK
    cost_per_donut = cost_per_dozen_donuts / donuts_per_dozen

    # L2
    sell_price_per_donut = 1 # sells each donut for $1
    profit_per_donut = sell_price_per_donut - cost_per_donut

    # L3
    goal_money = 96 # He wants to raise $96
    donuts_to_sell = goal_money / profit_per_donut

    # L4
    dozens_to_buy_and_sell = donuts_to_sell / donuts_per_dozen

    # FA
    answer = dozens_to_buy_and_sell
    return answer