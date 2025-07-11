def solve():
    """Index: 681.
    Returns: the total time it took Fernanda to finish the six audiobooks in days.
    """
    # L1
    audiobook_length_hours = 30 # each audiobook was 30 hours long
    daily_listening_hours = 2 # listened to 2 hours of an audiobook each day
    days_per_audiobook = audiobook_length_hours / daily_listening_hours

    # L2
    num_audiobooks = 6 # purchased six audiobooks
    total_days = num_audiobooks * days_per_audiobook

    # FA
    answer = total_days
    return answer