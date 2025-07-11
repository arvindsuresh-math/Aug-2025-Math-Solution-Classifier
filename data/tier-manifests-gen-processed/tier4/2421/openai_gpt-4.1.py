from fractions import Fraction

def solve():
    """Index: 2421.
    Returns: the total number of minutes it will take Charles to jog 6 miles.
    """
    # L1
    music_speed_mph = 6 # 6 MPH when he's got music on
    minutes_per_hour = 60 # WK
    music_speed_mpm = music_speed_mph / minutes_per_hour

    # L2
    album_length_min = 40 # album is 40 minutes long
    miles_with_music = album_length_min * music_speed_mpm

    # L3
    total_distance = 6 # jog 6 miles
    miles_without_music = total_distance - miles_with_music

    # L4
    no_music_speed_mph = 4 # 4 MPH when he doesn't
    no_music_speed_mpm = Fraction(no_music_speed_mph, minutes_per_hour)

    # L5
    time_without_music = miles_without_music / no_music_speed_mpm

    # L6
    total_time = album_length_min + time_without_music

    # FA
    answer = total_time
    return answer