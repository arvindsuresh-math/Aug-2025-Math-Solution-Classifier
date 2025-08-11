def solve():
    """Index: 163.
    Returns: the number of points James beat the old record by.
    """
    # L1
    touchdowns_per_game = 4 # scores 4 touchdowns per game
    points_per_touchdown = 6 # each touchdown is worth 6 points
    points_per_game = touchdowns_per_game * points_per_touchdown

    # L2
    games_in_season = 15 # 15 games in the season
    points_from_touchdowns = games_in_season * points_per_game

    # L3
    two_point_conversions = 6 # 2 point conversions 6 times during the season
    points_per_conversion = 2 # 2 point conversions (each worth 2 points)
    points_from_conversions = points_per_conversion * two_point_conversions

    # L4
    total_points = points_from_touchdowns + points_from_conversions

    # L5
    old_record = 300 # old record was 300 points
    points_beat_record = total_points - old_record

    # FA
    answer = points_beat_record
    return answer