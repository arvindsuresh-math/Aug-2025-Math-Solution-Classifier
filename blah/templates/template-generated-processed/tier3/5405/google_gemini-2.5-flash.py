def solve():
    """Index: 5405.
    Returns: the number of days it will take to complete the training.
    """
    # L1
    multiplication_minutes = 10 # 10 minutes
    division_minutes = 20 # 20 minutes
    daily_training_minutes = multiplication_minutes + division_minutes

    # L2
    total_training_hours = 5 # total of 5 hours
    minutes_per_hour = 60 # WK
    total_training_minutes_needed = total_training_hours * minutes_per_hour

    # L3
    total_days = total_training_minutes_needed / daily_training_minutes

    # FA
    answer = total_days
    return answer