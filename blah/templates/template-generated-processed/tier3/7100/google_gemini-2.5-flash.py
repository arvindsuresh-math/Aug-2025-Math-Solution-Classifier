def solve():
    """Index: 7100.
    Returns: the total number of words Gunther can type in a working day.
    """
    # L1
    total_working_minutes_per_day = 480 # he works 480 minutes per day
    minutes_per_set = 3 # every 3 minutes
    sets_of_words_per_day = total_working_minutes_per_day / minutes_per_set

    # L2
    words_per_set = 160 # 160 words every 3 minutes
    total_words_per_day = words_per_set * sets_of_words_per_day

    # FA
    answer = total_words_per_day
    return answer