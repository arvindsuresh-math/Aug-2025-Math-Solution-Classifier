def solve():
    """Index: 4639.
    Returns: the total number of points John scores.
    """
    # L1
    num_periods = 2 # 2 periods
    minutes_per_period = 12 # Each period is 12 minutes
    total_minutes_played = num_periods * minutes_per_period

    # L2
    shots_worth_2_points = 2 # 2 shots worth 2 points
    points_per_2_point_shot = 2 # 2 points
    points_from_2_point_shots = shots_worth_2_points * points_per_2_point_shot

    # L3
    points_from_3_point_shot = 3 # 1 shot worth 3 points
    points_per_interval = points_from_2_point_shots + points_from_3_point_shot

    # L4
    minutes_per_interval = 4 # every 4 minutes
    num_intervals = total_minutes_played / minutes_per_interval

    # L5
    total_points_scored = points_per_interval * num_intervals

    # FA
    answer = total_points_scored
    return answer