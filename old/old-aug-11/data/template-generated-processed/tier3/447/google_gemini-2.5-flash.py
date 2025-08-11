def solve():
    """Index: 447.
    Returns: the total number of books read by Megan, Kelcie, and Greg.
    """
    # L1
    megan_books = 32 # Megan has read 32 books this year
    kelcie_fraction_denominator = 4 # 1/4 the amount of books that Megan has read
    kelcie_books = megan_books / kelcie_fraction_denominator

    # L2
    greg_additional_books = 9 # 9 more
    greg_multiplier = 2 # twice the number of books
    greg_books = greg_additional_books + greg_multiplier * kelcie_books

    # L3
    total_books = megan_books + kelcie_books + greg_books

    # FA
    answer = total_books
    return answer