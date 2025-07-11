def solve():
    """Index: 2232.
    Returns: the total time Adam spent at school during the 3 days, in hours.
    """
    # L1
    monday_lessons = 6 # 6 lessons of 30 minutes each
    monday_lesson_minutes = 30 # 30 minutes each
    monday_minutes = monday_lessons * monday_lesson_minutes
    minutes_per_hour = 60 # WK
    monday_hours = monday_minutes // minutes_per_hour

    # L2
    tuesday_lessons = 3 # 3 lessons of 1 hour each
    tuesday_lesson_hours = 1 # 1 hour each
    tuesday_hours = tuesday_lessons * tuesday_lesson_hours
    wednesday_multiplier = 2 # twice as much time at school as on Tuesday
    wednesday_hours = wednesday_multiplier * tuesday_hours

    # L3
    total_hours = monday_hours + tuesday_hours + wednesday_hours

    # FA
    answer = total_hours
    return answer