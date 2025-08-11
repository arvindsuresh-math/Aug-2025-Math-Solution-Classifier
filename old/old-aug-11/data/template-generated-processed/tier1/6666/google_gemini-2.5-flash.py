def solve():
    """Index: 6666.
    Returns: the total hours David will spend on the course.
    """
    # L1
    class_duration_1 = 3 # 2 three-hour classes
    class_duration_2 = 3 # 2 three-hour classes
    class_duration_3 = 4 # 1 four-hour class
    weekly_class_hours = class_duration_1 + class_duration_2 + class_duration_3

    # L2
    homework_hours = 4 # 4 hours each week working on small group homework assignments
    total_weekly_hours = homework_hours + weekly_class_hours

    # L3
    course_duration_weeks = 24 # lasts for 24 weeks
    total_course_hours = total_weekly_hours * course_duration_weeks

    # FA
    answer = total_course_hours
    return answer