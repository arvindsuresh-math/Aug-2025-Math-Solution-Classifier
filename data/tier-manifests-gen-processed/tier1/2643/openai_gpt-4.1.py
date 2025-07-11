def solve():
    """Index: 2643.
    Returns: the total number of minutes Brian spends watching animal videos.
    """
    # L1
    cat_video_length = 4 # 4-minute video of cats
    dog_video_multiplier = 2 # video twice as long as the cat video
    dog_video_length = cat_video_length * dog_video_multiplier

    # L2
    first_two_total = cat_video_length + dog_video_length

    # L3
    gorilla_video_multiplier = 2 # twice as long as the previous two videos combined
    gorilla_video_length = first_two_total * gorilla_video_multiplier

    # L4
    total_time = gorilla_video_length + first_two_total

    # FA
    answer = total_time
    return answer