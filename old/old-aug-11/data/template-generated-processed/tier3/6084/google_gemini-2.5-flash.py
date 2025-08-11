def solve():
    """Index: 6084.
    Returns: the total number of books all the girls got combined.
    """
    # L1
    num_girls = 15 # 15 girls
    num_boys = 10 # 10 boys
    total_students = num_girls + num_boys

    # L2
    total_books = 375 # divided 375 books
    books_per_student = total_books / total_students

    # L3
    total_books_for_girls = num_girls * books_per_student

    # FA
    answer = total_books_for_girls
    return answer