def solve():
    """Index: 3158.
    Returns: the number of additional weeks Rex needs to continue taking lessons.
    """
    # L1
    hours_per_session = 2 # two-hour sessions
    sessions_per_week = 2 # twice a week
    lessons_per_week = hours_per_session * sessions_per_week

    # L2
    weeks_passed = 6 # After 6 weeks
    lessons_completed = lessons_per_week * weeks_passed

    # L3
    total_lessons_goal = 40 # 40 hour-long lessons
    lessons_remaining = total_lessons_goal - lessons_completed

    # L4
    weeks_needed = lessons_remaining / lessons_per_week

    # FA
    answer = weeks_needed
    return answer