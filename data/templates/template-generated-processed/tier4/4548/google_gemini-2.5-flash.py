def solve():
    """Index: 4548.
    Returns: the total time it would take John to read 3 books.
    """
    # L1
    speed_increase_decimal = 0.6 # 60% faster
    base_ratio = 1 # WK
    brother_time_multiplier = base_ratio + speed_increase_decimal

    # L2
    brother_time_per_book = 8 # 8 hours to read a book
    john_time_per_book = brother_time_per_book / brother_time_multiplier

    # L3
    num_books_john_reads = 3 # 3 books
    total_time_for_john = john_time_per_book * num_books_john_reads

    # FA
    answer = total_time_for_john
    return answer