def solve():
    """Index: 3495.
    Returns: the total number of goals the brothers have scored between them.
    """
    # L1
    louie_last_match_goals = 4 # scored four goals in the last hockey match
    brother_multiplier = 2 # twice as many goals
    brother_goals_per_game = brother_multiplier * louie_last_match_goals

    # L2
    brother_seasons = 3 # three seasons he's been on the team
    games_per_season = 50 # Each season has 50 games
    brother_total_games = brother_seasons * games_per_season

    # L3
    brother_total_goals = brother_goals_per_game * brother_total_games

    # L4
    louie_previous_goals = 40 # Louie scored 40 goals
    louie_total_goals = louie_previous_goals + louie_last_match_goals

    # L5
    total_goals_brothers = louie_total_goals + brother_total_goals

    # FA
    answer = total_goals_brothers
    return answer