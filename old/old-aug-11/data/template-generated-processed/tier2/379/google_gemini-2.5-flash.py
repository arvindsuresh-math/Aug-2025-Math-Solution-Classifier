def solve():
    """Index: 379.
    Returns: the total cost of everything.
    """
    # L1
    num_lessons = 20 # 20 lessons
    cost_per_lesson = 40 # $40 per lesson
    normal_lesson_price = num_lessons * cost_per_lesson

    # L2
    discount_percent = 0.25 # 25% discount
    discount_amount = normal_lesson_price * discount_percent

    # L3
    final_lesson_cost = normal_lesson_price - discount_amount

    # L4
    piano_cost = 500 # buys a piano for $500
    total_cost = piano_cost + final_lesson_cost

    # FA
    answer = total_cost
    return answer