from fractions import Fraction

def solve():
    """Index: 6844.
    Returns: the total number of songs Julia can download.
    """
    # L1
    minutes_per_hour = 60 # WK
    half_hour_fraction = Fraction(1, 2) # WK
    minutes_in_half_hour = half_hour_fraction * minutes_per_hour

    # L2
    seconds_per_minute = 60 # WK
    total_seconds = minutes_in_half_hour * seconds_per_minute

    # L3
    song_size_mb = 5 # size per song is 5MB
    internet_speed_mbps = 20 # internet speed is 20 MBps
    time_per_song_seconds = Fraction(song_size_mb, internet_speed_mbps)

    # L4
    inverse_time_per_song = 1 / time_per_song_seconds
    total_songs_downloaded = total_seconds * inverse_time_per_song

    # FA
    answer = total_songs_downloaded
    return answer