def solve():
    """Index: 4107.
    Returns: the length in seconds of each of the last two videos.
    """
    # L1
    first_video_minutes = 2 # The first video is 2 minutes long
    seconds_per_minute = 60 # WK
    first_video_seconds = first_video_minutes * seconds_per_minute

    # L2
    second_video_minutes = 4 # the second video is 4 minutes and 30 seconds
    second_video_additional_seconds = 30 # and 30 seconds
    second_video_minutes_in_seconds = second_video_minutes * seconds_per_minute
    second_video_seconds = second_video_minutes_in_seconds + second_video_additional_seconds

    # L3
    total_watch_time_seconds = 510 # total of 510 seconds watching YouTube
    combined_last_two_videos_seconds = total_watch_time_seconds - first_video_seconds - second_video_seconds

    # L4
    number_of_last_videos = 2 # the last two videos are equal in length
    each_last_video_length_seconds = combined_last_two_videos_seconds / number_of_last_videos

    # FA
    answer = each_last_video_length_seconds
    return answer