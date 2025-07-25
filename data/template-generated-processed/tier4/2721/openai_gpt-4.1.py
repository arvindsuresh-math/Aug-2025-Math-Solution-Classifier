def solve():
    """Index: 2721.
    Returns: the number of weeks Felicity has been collecting lollipops for.
    """
    # L1
    fort_total_sticks = 400 # The fort needs 400 sticks to finish it
    fort_completion_fraction = 0.6 # fort is 60% complete
    sticks_collected = fort_total_sticks * fort_completion_fraction

    # L2
    store_visits_per_week = 3 # family goes to the store three times a week and she always goes
    weeks_collecting = sticks_collected / store_visits_per_week

    # FA
    answer = weeks_collecting
    return answer