from fractions import Fraction

def solve():
    """Index: 2421.
    Returns: the total time to jog 6 miles.
    """
    # L1
    speed_music_mph = 6 # runs at 6 MPH when he's got music on
    minutes_per_hour = 60 # WK
    speed_music_mpm = speed_music_mph / minutes_per_hour

    # L2
    album_length_minutes = 40 # His album is 40 minutes long
    distance_with_music = album_length_minutes * speed_music_mpm

    # L3
    total_distance_miles = 6 # jog 6 miles
    remaining_distance = total_distance_miles - distance_with_music

    # L4
    speed_no_music_mph = 4 # 4 MPH when he doesn't
    speed_no_music_mpm = Fraction(speed_no_music_mph, minutes_per_hour)

    # L5
    time_no_music = remaining_distance / speed_no_music_mpm

    # L6
    total_time_minutes = album_length_minutes + time_no_music

    # FA
    answer = total_time_minutes
    return answer