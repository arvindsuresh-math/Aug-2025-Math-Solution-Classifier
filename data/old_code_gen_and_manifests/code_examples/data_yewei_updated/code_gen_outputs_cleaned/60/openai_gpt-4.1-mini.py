def solve(
    games_per_daughter: int = 8,  # They each have 8 games this season
    practice_hours_per_game: int = 4,  # Each team practices 4 hours for every game they play
    game_duration_hours: int = 2  # Each game lasts for 2 hours
):
    """Index: 60.
    Returns: the total hours Jerry spends watching his daughters play and practice.
    """
    #: L1
    hours_watching_one_daughter_games = games_per_daughter * game_duration_hours

    #: L2
    hours_watching_both_daughters_games = hours_watching_one_daughter_games * 2

    #: L3
    hours_watching_one_daughter_practice = games_per_daughter * practice_hours_per_game

    #: L4
    hours_watching_both_daughters_practice = hours_watching_one_daughter_practice * 2

    #: L5
    total_hours = hours_watching_both_daughters_games + hours_watching_both_daughters_practice

    answer = total_hours  # FINAL ANSWER
    return answer