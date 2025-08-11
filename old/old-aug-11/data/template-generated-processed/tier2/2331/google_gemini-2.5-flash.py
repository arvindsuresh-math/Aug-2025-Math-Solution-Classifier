def solve():
    """Index: 2331.
    Returns: the total number of words Henri reads.
    """
    # L1
    total_free_time = 8 # 8 hours to watch movies and read
    movie_one_duration = 3.5 # one movie that is 3.5 hours
    movie_two_duration = 1.5 # one movie that is 1.5 hours
    reading_time_hours = total_free_time - movie_one_duration - movie_two_duration

    # L2
    minutes_per_hour = 60 # WK
    reading_time_minutes = reading_time_hours * minutes_per_hour

    # L3
    reading_speed_wpm = 10 # read 10 words a minute
    total_words_read = reading_time_minutes * reading_speed_wpm

    # FA
    answer = total_words_read
    return answer