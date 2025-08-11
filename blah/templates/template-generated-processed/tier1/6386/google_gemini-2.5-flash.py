def solve():
    """Index: 6386.
    Returns: the total number of tokens Nathan used.
    """
    # L1
    air_hockey_games = 2 # played the air hockey game 2 times
    basketball_games = 4 # played the basketball game 4 times
    total_games = air_hockey_games + basketball_games

    # L2
    cost_per_game = 3 # each game cost 3 tokens
    total_tokens = total_games * cost_per_game

    # FA
    answer = total_tokens
    return answer