def solve():
    """Index: 379.
    Returns: the total cost for piano, lessons, and discount.
    """
    # L1
    num_lessons = 20 # 20 lessons
    lesson_price = 40 # $40 per lesson
    normal_lessons_cost = num_lessons * lesson_price

    # L2
    discount_percent = 0.25 # 25% discount
    discount_amount = normal_lessons_cost * discount_percent

    # L3
    discounted_lessons_cost = normal_lessons_cost - discount_amount

    # L4
    piano_cost = 500 # buys a piano for $500
    total_cost = piano_cost + discounted_lessons_cost

    # FA
    answer = total_cost
    return answer