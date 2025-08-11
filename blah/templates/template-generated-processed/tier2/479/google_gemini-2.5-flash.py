def solve():
    """Index: 479.
    Returns: the total number of hours Kat trains per week.
    """
    # L1
    strength_training_days_per_week = 3 # 3 times a week
    strength_training_hours_per_session = 1 # 1 hour in the gym
    strength_training_total_hours = strength_training_days_per_week * strength_training_hours_per_session

    # L2
    boxing_training_days_per_week = 4 # 4 times a week
    boxing_training_hours_per_session = 1.5 # 1.5 hours
    boxing_training_total_hours = boxing_training_days_per_week * boxing_training_hours_per_session

    # L3
    total_training_hours = strength_training_total_hours + boxing_training_total_hours

    # FA
    answer = total_training_hours
    return answer