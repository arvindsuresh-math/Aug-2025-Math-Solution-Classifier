def solve():
    """Index: 2331.
    Returns: the number of words Henri reads before his free time is up.
    """
    # L1
    total_free_hours = 8 # Henri has 8 hours to watch movies and read
    movie1_duration = 3.5 # one movie that is 3.5 hours
    movie2_duration = 1.5 # one movie that is 1.5 hours
    reading_hours = total_free_hours - movie1_duration - movie2_duration

    # L2
    minutes_per_hour = 60 # WK
    reading_minutes = reading_hours * minutes_per_hour

    # L3
    reading_rate = 10 # he can read 10 words a minute
    words_read = reading_minutes * reading_rate

    # FA
    answer = words_read
    return answer