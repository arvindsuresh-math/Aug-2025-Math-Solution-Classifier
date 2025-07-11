def solve():
    """Index: 347.
    Returns: the total number of songs Jeremy listened to in two days.
    """
    # L1
    songs_yesterday = 9 # he listened to nine songs
    fewer_songs = 5 # five fewer songs yesterday than today
    songs_today = songs_yesterday + fewer_songs

    # L2
    total_songs = songs_yesterday + songs_today

    # FA
    answer = total_songs
    return answer