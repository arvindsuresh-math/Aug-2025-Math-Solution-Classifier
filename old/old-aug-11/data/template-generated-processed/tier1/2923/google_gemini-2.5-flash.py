def solve():
    """Index: 2923.
    Returns: the total number of stamps Ruel has.
    """
    # L1
    num_books_10_stamps = 4 # four books
    stamps_per_book_10 = 10 # 10 stamps
    stamps_from_10_books = num_books_10_stamps * stamps_per_book_10

    # L2
    num_books_15_stamps = 6 # six books
    stamps_per_book_15 = 15 # 15 stamps
    stamps_from_15_books = num_books_15_stamps * stamps_per_book_15

    # L3
    total_stamps = stamps_from_10_books + stamps_from_15_books

    # FA
    answer = total_stamps
    return answer