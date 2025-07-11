def solve():
    """Index: 2405.
    Returns: the total time it takes for Lily to type the words.
    """
    # L1
    total_words = 255 # 255 words
    typing_speed = 15 # 15 words a minute
    typing_time_no_break = total_words / typing_speed

    # L2
    break_duration = 2 # a 2-minute break
    total_time = typing_time_no_break + break_duration

    # FA
    answer = total_time
    return answer