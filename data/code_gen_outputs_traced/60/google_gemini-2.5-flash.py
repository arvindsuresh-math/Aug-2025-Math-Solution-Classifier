def solve(
        num_daughters: int = 2, # Jerry’s two daughters
        games_per_season: int = 8, # They each have 8 games this season
        practice_hours_per_game: int = 4, # Each team practices 4 hours for every game they play
        game_duration_hours: int = 2 # each game lasts for 2 hours
    ):
    """Index: 60.
    Returns: the total hours Jerry will spend at the field watching his daughters play and practice.
    """
    #: L1
    hours_watching_one_daughter_play = games_per_season * game_duration_hours # eval: 16 = 8 * 2
    #: L2
    hours_watching_both_daughters_play = hours_watching_one_daughter_play * num_daughters # eval: 32 = 16 * 2
    #: L3
    hours_watching_one_daughter_practice = games_per_season * practice_hours_per_game # eval: 32 = 8 * 4
    #: L4
    hours_watching_both_daughters_practice = hours_watching_one_daughter_practice * num_daughters # eval: 64 = 32 * 2
    #: L5
    total_hours_at_field = hours_watching_both_daughters_play + hours_watching_both_daughters_practice # eval: 96 = 32 + 64
    answer = total_hours_at_field # FINAL ANSWER # eval: 96 = 96 # FINAL ANSWER
    return answer # eval: return 96