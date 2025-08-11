def solve():
    """Index: 60.
    Returns: the total number of hours Jerry will spend at the field watching his daughters play and practice altogether.
    """
    # L1
    games_per_daughter = 8 # each have 8 games this season
    hours_per_game = 2 # each game lasts for 2 hours
    play_hours_one = games_per_daughter * hours_per_game

    # L2
    num_daughters = 2 # Jerry's two daughters
    play_hours_both = play_hours_one * num_daughters

    # L3
    hours_practice_per_game = 4 # practices 4 hours for every game
    practice_hours_one = games_per_daughter * hours_practice_per_game

    # L4
    practice_hours_both = practice_hours_one * num_daughters

    # L5
    total_hours = play_hours_both + practice_hours_both

    # FA
    answer = total_hours
    return answer