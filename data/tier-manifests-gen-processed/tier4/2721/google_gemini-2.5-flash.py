def solve():
    """Index: 2721.
    Returns: the number of weeks Felicity has been collecting lollipops for.
    """
    # L1
    fort_total_sticks = 400 # The fort needs 400 sticks
    fort_completion_percent = 0.6 # fort is 60% complete
    current_sticks = fort_total_sticks * fort_completion_percent

    # L2
    trips_per_week = 3 # family goes to the store three times a week
    weeks_collecting = current_sticks / trips_per_week

    # FA
    answer = weeks_collecting
    return answer