def solve():
    """Index: 5126.
    Returns: the total cost for Micheal's piano lessons.
    """
    # L1
    total_hours = 18 # 18 hours of lessons
    hours_per_lesson = 1.5 # lasts for 1.5 hours
    num_lessons = total_hours / hours_per_lesson

    # L2
    cost_per_lesson = 30 # One lesson costs $30
    total_cost = num_lessons * cost_per_lesson

    # FA
    answer = total_cost
    return answer