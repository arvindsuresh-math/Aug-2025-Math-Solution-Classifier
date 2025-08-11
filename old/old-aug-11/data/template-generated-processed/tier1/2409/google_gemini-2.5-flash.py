def solve():
    """Index: 2409.
    Returns: the total number of songs they both listened to in that month.
    """
    # L1
    total_days_in_june = 30 # WK
    weekend_days_in_june = 8 # 8 weekend days in June
    playing_days_in_june = total_days_in_june - weekend_days_in_june

    # L2
    vivian_songs_per_day = 10 # 10 Spotify songs every day
    vivian_total_songs = vivian_songs_per_day * playing_days_in_june

    # L3
    clara_fewer_songs_per_day = 2 # 2 fewer songs each day
    clara_songs_per_day = vivian_songs_per_day - clara_fewer_songs_per_day

    # L4
    clara_total_songs = clara_songs_per_day * playing_days_in_june

    # L5
    total_songs_both = vivian_total_songs + clara_total_songs

    # FA
    answer = total_songs_both
    return answer