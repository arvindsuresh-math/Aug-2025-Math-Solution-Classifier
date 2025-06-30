def solve(
    num_daughters: int = 2, # Jerry’s two daughters
    games_per_season: int = 8, # They each have 8 games this season
    practice_hours_per_game: int = 4, # Each team practices 4 hours for every game they play
    game_duration_hours: int = 2 # If each game lasts for 2 hours
):
    """Index: 60.
    Returns: the total hours Jerry spends at the field watching his daughters play and practice.
    """

    #: L1
    game_hours_one_daughter = games_per_season * game_duration_hours # eval: 16 = 8 * 2

    #: L2
    total_game_hours = game_hours_one_daughter * num_daughters # eval: 32 = 16 * 2

    #: L3
    practice_hours_one_daughter = games_per_season * practice_hours_per_game # eval: 32 = 8 * 4

    #: L4
    total_practice_hours = practice_hours_one_daughter * num_daughters # eval: 64 = 32 * 2

    #: L5
    total_hours = total_game_hours + total_practice_hours # eval: 96 = 32 + 64

    #: FA
    answer = total_hours # eval: 96 = 96
    return answer # eval: return 96
