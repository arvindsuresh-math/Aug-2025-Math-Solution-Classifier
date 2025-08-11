def solve():
    """Index: 6254.
    Returns: the amount of money Geoffrey has left after the purchase.
    """
    # L1
    cost_per_game = 35 # 35 euros each
    num_games = 3 # 3 games
    total_game_cost = cost_per_game * num_games

    # L2
    initial_wallet_amount = 125 # he now has €125 in his wallet
    money_left = initial_wallet_amount - total_game_cost

    # FA
    answer = money_left
    return answer