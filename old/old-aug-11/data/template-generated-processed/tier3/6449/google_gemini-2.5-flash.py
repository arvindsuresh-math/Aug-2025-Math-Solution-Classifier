def solve():
    """Index: 6449.
    Returns: the average total number of goals scored by the team per game.
    """
    # L1
    carter_goals_per_game = 4 # scores 4 goals per game
    half_divisor = 2 # scores half as many as Carter
    shelby_goals_per_game = carter_goals_per_game / half_divisor

    # L2
    twice_multiplier = 2 # twice as many goals
    three_less = 3 # three less than twice as many
    judah_goals_per_game = (twice_multiplier * shelby_goals_per_game) - three_less

    # L3
    total_team_goals_per_game = carter_goals_per_game + shelby_goals_per_game + judah_goals_per_game

    # FA
    answer = total_team_goals_per_game
    return answer