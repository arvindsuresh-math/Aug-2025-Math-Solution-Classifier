def solve(
        num_daughters: int = 2, # Jerry's two daughters
        games_per_season: int = 8, # They each have 8 games this season
        practice_hours_per_game: int = 4, # Each team practices 4 hours for every game they play
        game_duration_hours: int = 2 # each game lasts for 2 hours
    ):
    """Index: 60.
    Returns: the total hours Jerry spends at the field watching his daughters play and practice.
    """
    #: L1
    hours_one_daughter_play_games = games_per_season * game_duration_hours

    #: L2
    total_hours_playing_games = hours_one_daughter_play_games * num_daughters

    #: L3
    hours_one_daughter_practice = games_per_season * practice_hours_per_game

    #: L4
    total_hours_practicing = hours_one_daughter_practice * num_daughters

    #: L5
    total_hours_at_field = total_hours_playing_games + total_hours_practicing

    answer = total_hours_at_field # FINAL ANSWER
    return answer