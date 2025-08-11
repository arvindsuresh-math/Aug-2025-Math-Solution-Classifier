def solve():
    """Index: 7083.
    Returns: the total number of books Lois has now.
    """
    # L1
    initial_books = 40 # Lois has 40 books
    nephew_fraction_denominator = 4 # a fourth of her books
    books_given_to_nephew = initial_books / nephew_fraction_denominator

    # L2
    books_after_nephew = initial_books - books_given_to_nephew

    # L3
    library_fraction_denominator = 3 # a third of her books
    books_donated_to_library = books_after_nephew / library_fraction_denominator

    # L4
    books_after_donation = books_after_nephew - books_donated_to_library

    # L5
    new_books_purchased = 3 # purchases 3 new books
    total_books_final = books_after_donation + new_books_purchased

    # FA
    answer = total_books_final
    return answer