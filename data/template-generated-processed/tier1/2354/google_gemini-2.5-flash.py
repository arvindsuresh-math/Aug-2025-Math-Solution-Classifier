def solve():
    """Index: 2354.
    Returns: the number of books remaining on the shelf after the second day.
    """
    # L1
    num_people_day1 = 5 # 5 people
    books_per_person_day1 = 2 # 2 books each
    books_borrowed_day1 = num_people_day1 * books_per_person_day1

    # L2
    books_borrowed_day2 = 20 # 20 more books are borrowed
    total_borrowed_books = books_borrowed_day1 + books_borrowed_day2

    # L3
    initial_novels = 100 # 100 historical novels
    remaining_books = initial_novels - total_borrowed_books

    # FA
    answer = remaining_books
    return answer