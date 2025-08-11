def solve():
    """Index: 447.
    Returns: the total number of books read by Megan, Kelcie, and Greg.
    """
    # L1
    megan_books = 32 # Megan has read 32 books this year
    kelcie_divisor = 4 # Kelcie has read 1/4 the amount
    kelcie_books = megan_books / kelcie_divisor

    # L2
    greg_multiplier = 2 # twice the number of books that Kelcie has read
    greg_increment = 9 # 9 more than twice
    greg_books = greg_increment + greg_multiplier * kelcie_books

    # L3
    total_books = megan_books + kelcie_books + greg_books

    # FA
    answer = total_books
    return answer