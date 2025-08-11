from fractions import Fraction

def solve():
    """Index: 2861.
    Returns: the number of additional games the team needs to win to make the playoffs.
    """
    # L1
    games_played = 20 # played 20 games
    games_left = 10 # 10 games left
    total_games = games_played + games_left

    # L2
    win_fraction = Fraction(2, 3) # win 2/3 of their games
    required_wins = total_games * win_fraction

    # L3
    games_won_so_far = 12 # won 12 of them
    additional_wins_needed = required_wins - games_won_so_far

    # FA
    answer = additional_wins_needed
    return answer