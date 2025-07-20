def solve():
    """Index: 7410.
    Returns: the total number of books Boris and Cameron have together after donating.
    """
    # L1
    boris_initial_books = 24 # Boris has 24 books
    boris_donation_denominator = 4 # a fourth of his books
    boris_donated_books = boris_initial_books / boris_donation_denominator

    # L2
    boris_remaining_books = boris_initial_books - boris_donated_books

    # L3
    cameron_initial_books = 30 # Cameron has 30 books
    cameron_donation_denominator = 3 # a third of his books
    cameron_donated_books = cameron_initial_books / cameron_donation_denominator

    # L4
    cameron_remaining_books = cameron_initial_books - cameron_donated_books

    # L5
    total_books_remaining = boris_remaining_books + cameron_remaining_books

    # FA
    answer = total_books_remaining
    return answer