def solve():
    """Index: 2062.
    Returns: the time Joan has left to use the special finger exerciser.
    """
    # L1
    total_hours = 2 # 2 hours to get all her music practice done
    minutes_per_hour = 60 # WK
    total_minutes_available = total_hours * minutes_per_hour

    # L2
    piano_time = 30 # 30 minutes on the piano
    writing_music_time = 25 # 25 minutes writing music on her computer
    reading_history_time = 38 # 38 minutes reading about the history of the piano
    total_minutes_spent = piano_time + writing_music_time + reading_history_time

    # L3
    remaining_time = total_minutes_available - total_minutes_spent

    # FA
    answer = remaining_time
    return answer