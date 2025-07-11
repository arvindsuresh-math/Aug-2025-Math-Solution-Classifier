def solve():
    """Index: 2997.
    Returns: the total number of hours Lila and Roger watched.
    """
    # L1
    video_length = 100 # 100 hours long
    lila_speed_multiplier = 2 # two times the average speed
    lila_watch_time_per_video = video_length / lila_speed_multiplier

    # L2
    num_videos_watched = 6 # watched six of the same videos
    lila_total_watch_time = lila_watch_time_per_video * num_videos_watched

    # L3
    roger_num_videos = 6 # watched six of the same videos
    normal_speed_video_length = 100 # 100 hours long
    roger_total_watch_time = roger_num_videos * normal_speed_video_length

    # L4
    total_hours_watched = roger_total_watch_time + lila_total_watch_time

    # FA
    answer = total_hours_watched
    return answer