def solve():
    """Index: 2062.
    Returns: the number of minutes Joan has left to use the finger exerciser.
    """
    # L1
    hours_available = 2 # 2 hours to get all her music practice done
    minutes_per_hour = 60 # WK
    total_minutes = hours_available * minutes_per_hour

    # L2
    piano_minutes = 30 # 30 minutes on the piano
    writing_minutes = 25 # 25 minutes writing music on her computer
    reading_minutes = 38 # 38 minutes reading about the history of the piano
    minutes_spent = piano_minutes + writing_minutes + reading_minutes

    # L3
    minutes_left = total_minutes - minutes_spent

    # FA
    answer = minutes_left
    return answer