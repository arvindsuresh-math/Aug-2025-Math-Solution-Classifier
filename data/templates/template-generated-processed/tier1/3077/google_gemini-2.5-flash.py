def solve():
    """Index: 3077.
    Returns: the total number of books remaining in the store.
    """
    # L1
    num_people_donating = 10 # ten people come
    books_per_person = 5 # donate five books each
    donated_books = num_people_donating * books_per_person

    # L2
    initial_donations = 300 # already received 300 book donations
    total_after_donations = initial_donations + donated_books

    # L3
    books_borrowed = 140 # a total of 140 books are borrowed
    remaining_books = total_after_donations - books_borrowed

    # FA
    answer = remaining_books
    return answer