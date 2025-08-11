def solve():
    """Index: 7272.
    Returns: the number of students the library can help on the fourth day.
    """
    # L1
    students_day1 = 4 # 4 students on the first day
    books_per_student = 5 # 5 books for their classes
    books_used_day1 = students_day1 * books_per_student

    # L2
    students_day2 = 5 # 5 students on the second day
    books_used_day2 = students_day2 * books_per_student

    # L3
    students_day3 = 6 # 6 students on the third day
    books_used_day3 = students_day3 * books_per_student

    # L4
    initial_total_books = 120 # 120 books
    books_remaining_day4 = initial_total_books - books_used_day1 - books_used_day2 - books_used_day3

    # L5
    students_can_be_helped_day4 = books_remaining_day4 / books_per_student

    # FA
    answer = students_can_be_helped_day4
    return answer