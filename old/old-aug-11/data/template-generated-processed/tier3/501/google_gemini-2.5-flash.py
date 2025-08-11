def solve():
    """Index: 501.
    Returns: the number of weeks it will take John to get to floor push-ups.
    """
    # L1
    days_per_stage = 15 # once he gets to 15 reps
    num_additional_stages = 3 # high elevation push-ups, low elevation push-ups, and floor push-ups
    total_days_for_progressions = days_per_stage * num_additional_stages

    # L2
    days_per_week_training = 5 # trains 5 days a week
    total_weeks = total_days_for_progressions / days_per_week_training

    # FA
    answer = total_weeks
    return answer