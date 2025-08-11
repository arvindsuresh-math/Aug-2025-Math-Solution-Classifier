def solve():
    """Index: 1981.
    Returns: the total memory space in MB occupied by the new songs.
    """
    # L1
    morning_songs = 10 # downloads 10 songs in the morning
    afternoon_songs = 15 # finds 15 more songs she likes so she downloads them
    night_songs = 3 # at night a friend of hers recommends 3 more songs she also downloads
    total_songs = morning_songs + afternoon_songs + night_songs

    # L2
    size_per_song = 5 # each song has a size of 5 MB
    total_size_mb = total_songs * size_per_song

    # FA
    answer = total_size_mb
    return answer