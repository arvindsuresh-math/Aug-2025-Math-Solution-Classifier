def solve():
    """Index: 1441.
    Returns: the total number of calories James burns per week.
    """
    # L1
    hours_per_class = 1.5 # works out for 1.5 hours each class
    minutes_per_hour = 60 # WK
    minutes_per_class = hours_per_class * minutes_per_hour

    # L2
    calories_per_minute = 7 # burns 7 calories per minute
    calories_per_class = minutes_per_class * calories_per_minute

    # L3
    classes_per_week = 3 # 3 times a week
    total_calories_per_week = calories_per_class * classes_per_week

    # FA
    answer = total_calories_per_week
    return answer