from fractions import Fraction

def solve():
    """Index: 5297.
    Returns: the total number of goals scored by the other players.
    """
    # L1
    total_players = 24 # A soccer team has 24 players
    fraction_of_players = Fraction(1, 3) # 1/3 of the players
    players_avg_1_goal = total_players * fraction_of_players

    # L2
    avg_goals_per_game = 1 # averaged 1 goal each per game
    total_goals_per_game_by_group = players_avg_1_goal * avg_goals_per_game

    # L3
    games_played = 15 # There have been 15 games played
    goals_by_group_1 = players_avg_1_goal * games_played

    # L4
    total_goals_season = 150 # scored 150 goals on the season
    goals_by_other_players = total_goals_season - goals_by_group_1

    # FA
    answer = goals_by_other_players
    return answer