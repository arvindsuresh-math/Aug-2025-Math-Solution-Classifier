def solve():
    """Index: 3348.
    Returns: the total number of songs Skyler wrote.
    """
    # L1
    hit_songs = 25 # 25 hit songs
    more_than_hit_songs = 10 # ten more songs
    top_100_songs = hit_songs + more_than_hit_songs

    # L2
    fewer_than_hit_songs = 5 # 5 fewer songs
    never_released_songs = hit_songs - fewer_than_hit_songs

    # L3
    total_songs = hit_songs + top_100_songs + never_released_songs

    # FA
    answer = total_songs
    return answer