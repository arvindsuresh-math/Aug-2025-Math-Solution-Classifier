def solve():
    """Index: 1021.
    Returns: the number of minutes Porche has left to get her project done.
    """
    # L1
    hours_available = 3 # 3 hours to get all her homework done
    minutes_per_hour = 60 # WK
    total_minutes = hours_available * minutes_per_hour

    # L2
    math_minutes = 45 # math homework takes her 45 minutes
    english_minutes = 30 # English homework takes her 30 minutes
    science_minutes = 50 # science homework takes her 50 minutes
    history_minutes = 25 # history homework takes her 25 minutes
    total_homework_minutes = math_minutes + english_minutes + science_minutes + history_minutes

    # L3
    minutes_left = total_minutes - total_homework_minutes

    # FA
    answer = minutes_left
    return answer