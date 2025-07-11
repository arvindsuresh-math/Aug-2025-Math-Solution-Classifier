def solve():
    """Index: 1481.
    Returns: the total hours Mike spends watching TV and playing video games.
    """
    # L1
    tv_hours_per_day = 4 # watches TV for 4 hours every day
    half_divisor = 2 # half as long as he watches TV
    video_game_hours_per_day = tv_hours_per_day / half_divisor

    # L2
    days_per_week = 7 # WK
    tv_hours_per_week = tv_hours_per_day * days_per_week

    # L3
    days_playing_video_games_per_week = 3 # If he plays video games 3 days a week
    total_video_game_hours_per_week = days_playing_video_games_per_week * video_game_hours_per_day

    # L4
    total_hours_spent = total_video_game_hours_per_week + tv_hours_per_week

    # FA
    answer = total_hours_spent
    return answer