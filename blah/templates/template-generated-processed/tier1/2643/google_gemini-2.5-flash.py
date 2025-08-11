def solve():
    """Index: 2643.
    Returns: the total number of minutes Brian spends watching animal videos.
    """
    # L1
    cat_video_duration = 4 # 4-minute video of cats
    multiplier_twice = 2 # twice as long
    dog_video_duration = cat_video_duration * multiplier_twice

    # L2
    first_two_combined_duration = cat_video_duration + dog_video_duration

    # L3
    gorilla_video_duration = first_two_combined_duration * multiplier_twice

    # L4
    total_watching_time = gorilla_video_duration + first_two_combined_duration

    # FA
    answer = total_watching_time
    return answer