def solve():
    """Index: 501.
    Returns: the number of weeks it will take John to get to floor push-ups.
    """
    # L1
    reps_per_stage = 15 # once he gets to 15 reps he will start training next type
    num_stages = 3 # high elevation, low elevation, floor push-ups
    total_progressions = reps_per_stage * num_stages

    # L2
    days_per_week = 5 # trains 5 days a week
    weeks_needed = total_progressions / days_per_week

    # FA
    answer = weeks_needed
    return answer