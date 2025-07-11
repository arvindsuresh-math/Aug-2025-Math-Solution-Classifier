def solve(
        games_per_daughter: int = 8,  # Each daughter has 8 games this season
        game_duration: int = 2,  # Each game lasts for 2 hours
        practice_hours_per_game: int = 4,  # Each team practices 4 hours for every game
        num_daughters: int = 2  # Jerry has two daughters
    ):
    """Index: 60.
    Returns: the total hours Jerry will spend at the field watching his daughters play and practice.
    """

    #: L1
    hours_watching_one_daughter_games = games_per_daughter * game_duration # eval: 16 = 8 * 2

    #: L2
    hours_watching_both_daughters_games = hours_watching_one_daughter_games * num_daughters # eval: 32 = 16 * 2

    #: L3
    hours_watching_one_daughter_practice = 31 # eval: 31 = 31

    #: L4
    hours_watching_both_daughters_practice = hours_watching_one_daughter_practice * num_daughters # eval: 62 = 31 * 2

    #: L5
    total_hours_at_field = hours_watching_both_daughters_games + hours_watching_both_daughters_practice # eval: 94 = 32 + 62

    #: FA
    answer = total_hours_at_field
    return answer # eval: return 94
