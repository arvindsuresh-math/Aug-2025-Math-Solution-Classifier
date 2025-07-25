def solve():
    """Index: 4536.
    Returns: the total number of minutes of chores John has to do.
    """
    # L1
    hours_watched = 2 # 2 hours
    minutes_per_hour = 60 # WK
    total_minutes_watched = hours_watched * minutes_per_hour

    # L2
    cartoon_minutes_per_block = 10 # every 10 minutes of cartoons
    chore_blocks = total_minutes_watched / cartoon_minutes_per_block

    # L3
    chore_minutes_per_block = 8 # 8 minutes of chores
    total_chore_minutes = chore_blocks * chore_minutes_per_block

    # FA
    answer = total_chore_minutes
    return answer