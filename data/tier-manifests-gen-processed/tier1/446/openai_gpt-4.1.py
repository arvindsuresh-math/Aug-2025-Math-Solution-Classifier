def solve():
    """Index: 446.
    Returns: the total number of books in the classroom altogether.
    """
    # L1
    num_children = 10 # 10 children
    books_per_child = 7 # 7 books each
    children_books = num_children * books_per_child

    # L2
    teacher_books = 8 # teacher brings another 8 books
    total_books = children_books + teacher_books

    # FA
    answer = total_books
    return answer