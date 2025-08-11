def solve():
    """Index: 6798.
    Returns: the total minutes Lena and her brother played video games.
    """
    # L1
    lena_hours_played = 3.5 # 3.5 hours last weekend
    minutes_per_hour = 60 # WK
    lena_minutes_played = lena_hours_played * minutes_per_hour

    # L2
    brother_more_minutes = 17 # 17 minutes more than she did
    brother_minutes_played = lena_minutes_played + brother_more_minutes

    # L3
    total_minutes_played = lena_minutes_played + brother_minutes_played

    # FA
    answer = total_minutes_played
    return answer