def solve():
    """Index: 2011.
    Returns: the total cost in dollars.
    """
    # L1
    num_friends = 4 # 4 friends
    games_per_friend = 60 # 60 games each
    total_games = num_friends * games_per_friend

    # L2
    tokens_per_game = 2 # Each game costs 2 tokens
    total_tokens_needed = tokens_per_game * total_games

    # L3
    cost_per_dollar_tokens = 30 # 30 for $1
    total_cost = total_tokens_needed / cost_per_dollar_tokens

    # FA
    answer = total_cost
    return answer