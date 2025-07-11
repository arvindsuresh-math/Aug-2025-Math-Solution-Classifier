def solve():
    """Index: 162.
    Returns: the total amount Daniel spent on all games.
    """
    # L1
    num_games_batch1 = 80 # 80 of them
    price_per_game_batch1 = 12 # $12 each
    cost_batch1 = num_games_batch1 * price_per_game_batch1

    # L2
    total_games = 346 # collection of 346 video games
    remaining_games = total_games - num_games_batch1

    # L3
    percentage_batch2_numerator = 50 # 50%
    percentage_batch2_denominator = 100 # 50%
    num_games_batch2 = percentage_batch2_numerator / percentage_batch2_denominator * remaining_games

    # L4
    price_per_game_batch2 = 7 # $7
    cost_batch2 = num_games_batch2 * price_per_game_batch2

    # L5
    num_games_batch3 = remaining_games - num_games_batch2 # The other 133 games
    price_per_game_batch3 = 3 # $3 each
    cost_batch3 = num_games_batch3 * price_per_game_batch3

    # L6
    total_spent = cost_batch1 + cost_batch2 + cost_batch3

    # FA
    answer = total_spent
    return answer