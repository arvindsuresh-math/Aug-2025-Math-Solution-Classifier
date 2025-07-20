def solve():
    """Index: 5523.
    Returns: the number of months Joe can buy and sell games before running out of money.
    """
    # L1
    cost_to_buy_game = 50 # spends $50 a month on video games
    price_to_sell_game = 30 # sells his games for $30 each
    monthly_loss = cost_to_buy_game - price_to_sell_game

    # L2
    initial_money = 240 # starts with $240
    months_until_out_of_money = initial_money / monthly_loss

    # FA
    answer = months_until_out_of_money
    return answer