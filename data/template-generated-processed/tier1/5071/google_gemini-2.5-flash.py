def solve():
    """Index: 5071.
    Returns: the amount of money left in the club register in millions of dollars.
    """
    # L1
    players_sold = 2 # sells 2 of its players
    sale_price_per_player = 10 # at $10 million each
    total_sale_money = players_sold * sale_price_per_player

    # L2
    initial_balance = 100 # balance of $100 million
    balance_after_sale = initial_balance + total_sale_money

    # L3
    players_bought = 4 # buys 4 more
    buy_price_per_player = 15 # at $15 million each
    total_buy_cost = players_bought * buy_price_per_player

    # L4
    final_balance = balance_after_sale - total_buy_cost

    # FA
    answer = final_balance
    return answer