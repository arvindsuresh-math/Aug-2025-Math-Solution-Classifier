def solve():
    """Index: 2362.
    Returns: the total number of minutes of video John releases per week.
    """
    # L1
    short_video_length = 2 # short 2 minute videos
    long_video_multiplier = 6 # 1 of them is 6 times as long
    long_video_length = short_video_length * long_video_multiplier

    # L2
    num_short_videos = 2 # Two of them are short
    num_long_videos = 1 # 1 of them is long
    daily_minutes = num_short_videos * short_video_length + num_long_videos * long_video_length

    # L3
    days_per_week = 7 # 7-day week
    weekly_minutes = daily_minutes * days_per_week

    # FA
    answer = weekly_minutes
    return answer