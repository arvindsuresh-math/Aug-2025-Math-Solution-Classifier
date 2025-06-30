def solve(
    num_daughters: int = 2, # Jerry’s two daughters
    games_per_daughter: int = 8, # They each have 8 games this season
    practice_hours_per_game: int = 4, # Each team practices 4 hours for every game they play
    game_duration: int = 2 # each game lasts for 2 hours
):
    """Index: 60.
    Returns: the total number of hours Jerry will spend at the field watching his daughters play and practice altogether.
    """

    #: L1
    hours_watching_one_daughter_play = games_per_daughter * game_duration

    #: L2
    total_hours_watching_games = hours_watching_one_daughter_play * num_daughters

    #: L3
    hours_watching_one_daughter_practice = games_per_daughter * practice_hours_per_game

    #: L4
    total_hours_watching_practice = hours_watching_one_daughter_play * num_daughters

    #: L5
    total_hours_at_field = total_hours_watching_games + total_hours_watching_practice

    #: FA
    answer = total_hours_at_field
    return answer