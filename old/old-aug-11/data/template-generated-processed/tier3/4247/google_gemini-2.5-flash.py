def solve():
    """Index: 4247.
    Returns: the average number of minutes each player gets.
    """
    # L1
    point_guard_seconds = 130 # 130 seconds of the point guard
    shooting_guard_seconds = 145 # 145 seconds of the shooting guard
    small_forward_seconds = 85 # 85 seconds of the small forward
    power_forward_seconds = 60 # 60 seconds of the power forward
    center_seconds = 180 # 180 seconds of the center
    total_movie_seconds = point_guard_seconds + shooting_guard_seconds + small_forward_seconds + power_forward_seconds + center_seconds

    # L2
    seconds_per_minute = 60 # WK
    total_movie_minutes = total_movie_seconds / seconds_per_minute

    # L3
    number_of_players = 5 # every player (5 positions listed)
    average_minutes_per_player = total_movie_minutes / number_of_players

    # FA
    answer = average_minutes_per_player
    return answer