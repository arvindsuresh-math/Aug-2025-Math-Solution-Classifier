def solve():
    """Index: 1021.
    Returns: the time Porche has left for her project.
    """
    # L1
    total_hours_available = 3 # 3 hours to get all her homework done
    minutes_per_hour = 60 # WK
    total_minutes_available = total_hours_available * minutes_per_hour

    # L2
    math_homework_minutes = 45 # 45 minutes
    english_homework_minutes = 30 # 30 minutes
    science_homework_minutes = 50 # 50 minutes
    history_homework_minutes = 25 # 25 minutes
    total_homework_minutes_spent = math_homework_minutes + english_homework_minutes + science_homework_minutes + history_homework_minutes

    # L3
    time_left_for_project = total_minutes_available - total_homework_minutes_spent

    # FA
    answer = time_left_for_project
    return answer