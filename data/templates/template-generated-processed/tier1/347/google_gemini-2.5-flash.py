def solve():
    """Index: 347.
    Returns: the total number of songs Jeremy listened to in two days.
    """
    # L1
    songs_yesterday = 9 # listened to nine songs
    fewer_than_today = 5 # five fewer songs yesterday than today
    songs_today = songs_yesterday + fewer_than_today

    # L2
    total_songs_two_days = songs_yesterday + songs_today

    # FA
    answer = total_songs_two_days
    return answer