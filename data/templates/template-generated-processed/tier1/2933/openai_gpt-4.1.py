def solve():
    """Index: 2933.
    Returns: the number of books in the library now.
    """
    # L1
    initial_books = 235 # 235 books in a library
    tuesday_taken = 227 # 227 books are taken out
    after_tuesday = initial_books - tuesday_taken

    # L2
    thursday_brought_back = 56 # 56 books are brought back
    after_thursday = after_tuesday + thursday_brought_back

    # L3
    friday_taken = 35 # 35 books are taken out again on Friday
    after_friday = after_thursday - friday_taken

    # FA
    answer = after_friday
    return answer