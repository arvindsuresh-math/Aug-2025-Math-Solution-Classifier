def solve():
    """Index: 2923.
    Returns: the total number of stamps Ruel has.
    """
    # L1
    num_books_10 = 4 # four books of 10 stamps
    stamps_per_book_10 = 10 # four books of 10 stamps
    stamps_from_10 = num_books_10 * stamps_per_book_10

    # L2
    num_books_15 = 6 # six books of 15 stamps
    stamps_per_book_15 = 15 # six books of 15 stamps
    stamps_from_15 = num_books_15 * stamps_per_book_15

    # L3
    total_stamps = stamps_from_10 + stamps_from_15

    # FA
    answer = total_stamps
    return answer