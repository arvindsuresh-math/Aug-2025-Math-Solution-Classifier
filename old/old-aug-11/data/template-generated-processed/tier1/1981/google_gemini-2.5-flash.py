def solve():
    """Index: 1981.
    Returns: the total memory space in MB the new songs will occupy.
    """
    # L1
    songs_morning = 10 # downloads 10 songs in the morning
    songs_later = 15 # finds 15 more songs
    songs_night = 3 # recommends 3 more songs
    total_songs = songs_morning + songs_later + songs_night

    # L2
    memory_per_song = 5 # each song has a size of 5 MB
    total_memory_space = total_songs * memory_per_song

    # FA
    answer = total_memory_space
    return answer