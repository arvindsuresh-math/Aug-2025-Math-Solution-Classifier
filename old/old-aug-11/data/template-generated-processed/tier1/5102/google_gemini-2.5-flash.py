def solve():
    """Index: 5102.
    Returns: the total number of books the three have.
    """
    # L1
    darryl_books = 20 # Darryl has 20 books
    twice_multiplier = 2 # twice the number of books
    lamont_books = darryl_books * twice_multiplier

    # L2
    darryl_lamont_total = lamont_books + darryl_books

    # L3
    loris_needs_more = 3 # Loris needs three more books
    loris_books = lamont_books - loris_needs_more

    # L4
    total_books_three = darryl_lamont_total + loris_books

    # FA
    answer = total_books_three
    return answer