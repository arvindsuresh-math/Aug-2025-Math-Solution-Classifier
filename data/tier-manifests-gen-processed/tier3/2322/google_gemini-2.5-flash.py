def solve():
    """Index: 2322.
    Returns: the average touchdowns per game Richard must score in the final two games to beat Archie's record.
    """
    # L1
    games_played = 14 # first 14 games
    avg_touchdowns_per_game = 6 # averaged 6 touchdowns a game
    touchdowns_scored_so_far = games_played * avg_touchdowns_per_game

    # L2
    archie_record = 89 # Archie holds the school record for most touchdown passes with 89
    to_beat_record_margin = 1 # WK
    touchdowns_to_beat_record = archie_record + to_beat_record_margin

    # L3
    touchdowns_needed = touchdowns_to_beat_record - touchdowns_scored_so_far

    # L4
    total_games_season = 16 # season of 16 games
    games_left = total_games_season - games_played

    # L5
    avg_touchdowns_needed_per_game = touchdowns_needed / games_left

    # FA
    answer = avg_touchdowns_needed_per_game
    return answer