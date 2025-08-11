from fractions import Fraction

def solve():
    """Index: 6423.
    Returns: the number of remaining games the team must win.
    """
    # L1
    games_played = 50 # 50 games that they have played
    games_left = 25 # 25 games left to play
    total_games_season = games_played + games_left

    # L2
    target_win_percentage = Fraction(64, 100) # 64%
    target_wins = total_games_season * target_win_percentage

    # L3
    games_already_won = 35 # won 35 out of the 50 games
    games_to_win = target_wins - games_already_won

    # FA
    answer = games_to_win
    return answer