def solve(
    games_per_daughter: int = 8,  # each daughter has 8 games
    hours_per_game: int = 2,      # each game lasts 2 hours
    practice_hours_per_game: int = 4  # each team practices 4 hours for every game
):
    """Index: 60.
    Returns: the total hours Jerry spends watching his daughters play and practice.
    """
    #: L1
    hours_watching_one_daughter_games = games_per_daughter * hours_per_game # eval: 16 = 8 * 2
    #: L2
    hours_watching_both_daughters_games = hours_watching_one_daughter_games * 2 # eval: 32 = 16 * 2
    #: L3
    hours_watching_one_daughter_practice = games_per_daughter * practice_hours_per_game # eval: 32 = 8 * 4
    #: L4
    hours_watching_both_daughters_practice = hours_watching_one_daughter_practice * 2 # eval: 64 = 32 * 2
    #: L5
    total_hours = hours_watching_both_daughters_games + hours_watching_both_daughters_practice # eval: 96 = 32 + 64
    answer = total_hours  # FINAL ANSWER # eval: 96 = 96  # FINAL ANSWER
    return answer # eval: return 96