def solve():
    """Index: 5031.
    Returns: the total time Gretchen spends walking in minutes.
    """
    # L1
    sitting_hours = 6 # 6 hours working at her desk
    minutes_per_hour = 60 # WK
    total_sitting_minutes = sitting_hours * minutes_per_hour

    # L2
    sitting_interval_minutes = 90 # 90 minutes you spend sitting
    num_walking_breaks = total_sitting_minutes / sitting_interval_minutes

    # L3
    walking_break_duration = 10 # 10 minutes walking
    total_walking_minutes = num_walking_breaks * walking_break_duration

    # FA
    answer = total_walking_minutes
    return answer