def solve():
    """Index: 2409.
    Returns: the total number of songs Vivian and Clara listened to in June.
    """
    # L1
    june_days = 30 # June has 30 days
    weekend_days = 8 # there were 8 weekend days in June
    active_days = june_days - weekend_days

    # L2
    vivian_per_day = 10 # Vivian plays 10 Spotify songs every day
    vivian_total = vivian_per_day * active_days

    # L3
    clara_fewer = 2 # Clara plays 2 fewer songs each day
    clara_per_day = vivian_per_day - clara_fewer

    # L4
    clara_total = clara_per_day * active_days

    # L5
    total_songs = vivian_total + clara_total

    # FA
    answer = total_songs
    return answer