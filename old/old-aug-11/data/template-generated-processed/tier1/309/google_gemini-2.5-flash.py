def solve():
    """Index: 309.
    Returns: the total number of words Carl can type in 7 days.
    """
    # L1
    words_per_minute = 50 # 50 words per minute
    minutes_per_hour = 60 # WK
    words_per_hour = words_per_minute * minutes_per_hour

    # L2
    hours_per_day = 4 # 4 hours per day
    words_per_day = words_per_hour * hours_per_day

    # L3
    number_of_days = 7 # 7 days
    total_words = words_per_day * number_of_days

    # FA
    answer = total_words
    return answer