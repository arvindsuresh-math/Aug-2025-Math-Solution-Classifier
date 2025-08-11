def solve():
    """Index: 2362.
    Returns: the total minutes of video John releases per week.
    """
    # L1
    short_video_duration = 2 # 2 minute videos
    long_video_multiplier = 6 # 6 times as long
    long_video_duration = short_video_duration * long_video_multiplier

    # L2
    daily_minutes = short_video_duration + short_video_duration + long_video_duration

    # L3
    days_in_week = 7 # 7-day week
    weekly_minutes = daily_minutes * days_in_week

    # FA
    answer = weekly_minutes
    return answer