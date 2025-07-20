def solve():
    """Index: 5804.
    Returns: the typical number of rap songs Ziggy gets requested every night.
    """
    # L1
    total_requests = 30 # 30 song requests every night
    electropop_divisor = 2 # Half the songs requested
    electropop_requests = total_requests / electropop_divisor

    # L2
    dance_divisor = 3 # A third of that amount
    dance_requests = electropop_requests / dance_divisor

    # L3
    rock_music_requests = 5 # Five song requests are rock music
    oldies_less_than_rock = 3 # three less in number than rock requests
    oldies_requests = rock_music_requests - oldies_less_than_rock

    # L4
    dj_choice_divisor = 2 # half the number of times he plays an oldie
    dj_choice_requests = oldies_requests / dj_choice_divisor

    # L5
    rap_songs_requested = total_requests - electropop_requests - dance_requests - rock_music_requests - oldies_requests - dj_choice_requests

    # FA
    answer = rap_songs_requested
    return answer