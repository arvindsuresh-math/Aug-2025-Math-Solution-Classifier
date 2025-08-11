def solve():
    """Index: 4995.
    Returns: the total amount John pays for music a year.
    """
    # L1
    hours_per_month = 20 # 20 hours of music a month
    minutes_per_hour = 60 # WK
    minutes_per_month = hours_per_month * minutes_per_hour

    # L2
    avg_song_length_minutes = 3 # The average length of a song is 3 minutes
    songs_per_month = minutes_per_month / avg_song_length_minutes

    # L3
    cost_per_song = 0.50 # He buys each song for $.50
    cost_per_month = songs_per_month * cost_per_song

    # L4
    months_per_year = 12 # WK
    cost_per_year = cost_per_month * months_per_year

    # FA
    answer = cost_per_year
    return answer