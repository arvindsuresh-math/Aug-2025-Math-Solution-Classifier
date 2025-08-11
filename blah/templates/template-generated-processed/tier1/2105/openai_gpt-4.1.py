def solve():
    """Index: 2105.
    Returns: the total amount Tom pays for his dance lessons.
    """
    # L1
    total_lessons = 10 # 10 dance lessons
    free_lessons = 2 # two of them for free
    paid_lessons = total_lessons - free_lessons

    # L2
    cost_per_lesson = 10 # cost $10 each
    total_cost = paid_lessons * cost_per_lesson

    # FA
    answer = total_cost
    return answer