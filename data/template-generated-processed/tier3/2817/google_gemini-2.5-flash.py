def solve():
    """Index: 2817.
    Returns: the number of minutes it took Elvis to write each song.
    """
    # L1
    studio_hours = 5 # He spends 5 hours in the studio
    minutes_per_hour = 60 # WK
    total_studio_minutes = studio_hours * minutes_per_hour

    # L2
    minutes_per_song_record = 12 # Each song takes 12 minutes to record
    num_songs = 10 # 10 songs
    total_recording_minutes = minutes_per_song_record * num_songs

    # L3
    total_editing_minutes = 30 # it takes 30 minutes to edit all of his songs
    remaining_writing_minutes = total_studio_minutes - total_recording_minutes - total_editing_minutes

    # L4
    minutes_per_song_write = remaining_writing_minutes / num_songs

    # FA
    answer = minutes_per_song_write
    return answer