def solve():
    """Index: 4646.
    Returns: the average passing yards per game Tom Brady needs.
    """
    # L1
    record_value = 5999 # The current record is 5999 yards
    yards_to_beat_record = 1 # WK
    record_to_beat = record_value + yards_to_beat_record
    current_yards = 4200 # He currently has 4200 yards
    yards_needed = record_to_beat - current_yards

    # L2
    games_left = 6 # with 6 games left in the season
    yards_per_game_needed = yards_needed / games_left

    # FA
    answer = yards_per_game_needed
    return answer