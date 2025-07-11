def solve():
    """Index: 1244.
    Returns: the total number of hours taken to complete the 3 songs.
    """
    # L1
    hours_per_day_per_song = 10 # 10 hours a day
    days_per_song = 10 # each song took 10 days
    hours_per_song = hours_per_day_per_song * days_per_song

    # L2
    num_songs = 3 # 3 songs
    total_hours = num_songs * hours_per_song

    # FA
    answer = total_hours
    return answer