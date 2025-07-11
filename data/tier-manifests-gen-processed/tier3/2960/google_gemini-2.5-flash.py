def solve():
    """Index: 2960.
    Returns: the time in hours it takes Emily to write the words.
    """
    # L1
    words_per_minute = 60 # Emily can type 60 words per minute
    minutes_per_hour = 60 # WK
    words_per_hour = words_per_minute * minutes_per_hour

    # L2
    total_words = 10800 # write 10,800 words
    time_in_hours = total_words / words_per_hour

    # FA
    answer = time_in_hours
    return answer