def solve(
        games_per_daughter: int = 8,  # Each daughter has 8 games this season
        hours_per_game: int = 2,  # Each game lasts for 2 hours
        practice_hours_per_game: int = 4  # Each team practices 4 hours for every game
    ):
    """Index: 60.
    Returns: the total hours Jerry will spend at the field watching his daughters play and practice.
    """
    #: L1
    hours_watching_one_daughter_games = games_per_daughter * hours_per_game

    #: L2
    hours_watching_both_daughters_games = hours_watching_one_daughter_games * 2

    #: L3
    hours_watching_one_daughter_practice = games_per_daughter * practice_hours_per_game

    #: L4
    hours_watching_both_daughters_practice = hours_watching_one_daughter_practice * 2

    #: L5
    total_hours_at_field = hours_watching_both_daughters_games + hours_watching_both_daughters_practice

    answer = total_hours_at_field  # FINAL ANSWER
    return answer