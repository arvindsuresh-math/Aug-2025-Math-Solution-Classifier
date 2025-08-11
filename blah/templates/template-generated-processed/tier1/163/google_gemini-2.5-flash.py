def solve():
    """Index: 163.
    Returns: the number of points James beat the old record by.
    """
    # L1
    touchdowns_per_game = 4 # scores 4 touchdowns per game
    points_per_touchdown = 6 # each touchdown is worth 6 points
    points_per_game_from_touchdowns = touchdowns_per_game * points_per_touchdown

    # L2
    num_games_in_season = 15 # 15 games in the season
    total_points_from_touchdowns = num_games_in_season * points_per_game_from_touchdowns

    # L3
    points_per_conversion = 2 # score 2 point conversions
    num_conversions = 6 # 6 times during the season
    total_points_from_conversions = points_per_conversion * num_conversions

    # L4
    james_total_points = total_points_from_touchdowns + total_points_from_conversions

    # L5
    old_record_points = 300 # The old record was 300 points
    points_beat_record_by = james_total_points - old_record_points

    # FA
    answer = points_beat_record_by
    return answer