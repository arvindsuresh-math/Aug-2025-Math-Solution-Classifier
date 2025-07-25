def solve():
    """Index: 1374.
    Returns: the total number of books the three people have.
    """
    # L1
    darla_books = 6 # 6 books in her locker

    # L2
    half_divisor = 2 # half as many books
    katie_books = darla_books / half_divisor

    # L3
    gary_multiplier = 5 # 5 times the number of books
    gary_books = gary_multiplier * (darla_books + katie_books)

    # L4
    total_books = darla_books + katie_books + gary_books

    # FA
    answer = total_books
    return answer