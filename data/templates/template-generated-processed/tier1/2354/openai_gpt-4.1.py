def solve():
    """Index: 2354.
    Returns: the number of books remaining on the shelf after the second day.
    """
    # L1
    num_people_first_day = 5 # 5 people borrow 2 books each
    books_per_person = 2 # 2 books each
    books_borrowed_first_day = num_people_first_day * books_per_person

    # L2
    books_borrowed_second_day = 20 # 20 more books are borrowed on the second day
    total_books_borrowed = books_borrowed_first_day + books_borrowed_second_day

    # L3
    total_books_on_shelf = 100 # a collection of 100 historical novels
    books_remaining = total_books_on_shelf - total_books_borrowed

    # FA
    answer = books_remaining
    return answer