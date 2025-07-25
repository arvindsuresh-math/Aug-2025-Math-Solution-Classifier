from fractions import Fraction

def solve():
    """Index: 1140.
    Returns: the number of games the team can lose.
    """
    # L1
    initial_games_played = 40 # played 40 games
    win_percentage_initial = Fraction(70, 100) # won 70% of the games
    games_won_initial = initial_games_played * win_percentage_initial

    # L2
    remaining_games = 10 # still had 10 games to play
    total_games_overall = initial_games_played + remaining_games

    # L3
    target_win_percentage = Fraction(60, 100) # win 60% of their games
    target_wins_total = total_games_overall * target_win_percentage

    # L4
    games_to_win_additionally = target_wins_total - games_won_initial

    # L5
    games_can_lose = remaining_games - games_to_win_additionally

    # FA
    answer = games_can_lose
    return answer