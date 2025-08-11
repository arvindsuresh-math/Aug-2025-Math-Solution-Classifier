def solve():
    """Index: 60.
    Returns: the total hours Jerry will spend at the field watching his daughters play and practice.
    """
    # L1
    games_per_daughter = 8 # 8 games this season
    game_duration_hours = 2 # each game lasts for 2 hours
    hours_one_daughter_games = games_per_daughter * game_duration_hours

    # L2
    num_daughters = 2 # Jerry’s two daughters
    hours_both_daughters_games = hours_one_daughter_games * num_daughters

    # L3
    practice_hours_per_game = 4 # practices 4 hours for every game
    hours_one_daughter_practice = games_per_daughter * practice_hours_per_game

    # L4
    hours_both_daughters_practice = hours_one_daughter_practice * num_daughters

    # L5
    total_hours = hours_both_daughters_games + hours_both_daughters_practice

    # FA
    answer = total_hours
    return answer