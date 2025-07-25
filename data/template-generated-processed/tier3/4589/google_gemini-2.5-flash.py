def solve():
    """Index: 4589.
    Returns: the total time spent cleaning up in minutes.
    """
    # L1
    seconds_per_minute = 60 # WK
    time_per_egg_seconds = 15 # 15 seconds cleaning up each egg
    eggs_per_minute = seconds_per_minute / time_per_egg_seconds

    # L2
    total_eggs = 60 # 60 eggs
    time_for_eggs = total_eggs / eggs_per_minute

    # L3
    total_tp_rolls = 7 # 7 rolls of toilet paper
    time_per_tp_roll_minutes = 30 # 30 minutes cleaning up each roll of toilet paper
    time_for_tp = total_tp_rolls * time_per_tp_roll_minutes

    # L4
    total_cleaning_time = time_for_tp + time_for_eggs

    # FA
    answer = total_cleaning_time
    return answer