def solve():
    """Index: 2032.
    Returns: the number of books now in the library.
    """
    # L1
    initial_books = 250 # 250 books inside a library
    tuesday_taken = 120 # 120 books are taken out
    after_tuesday = initial_books - tuesday_taken

    # L2
    wednesday_returned = 35 # 35 books are returned
    after_wednesday = after_tuesday + wednesday_returned

    # L3
    thursday_taken = 15 # 15 books are withdrawn from the library
    after_thursday = after_wednesday - thursday_taken

    # FA
    answer = after_thursday
    return answer