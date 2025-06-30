def solve(
    num_history_books: int = 12, # She shelved 12 history books
    num_romance_books: int = 8, # 8 romance books
    num_poetry_books: int = 4, # and 4 poetry books
    num_western_novels: int = 5, # including 5 Western novels
    num_biographies: int = 6 # and 6 biographies
):
    """Index: 97.
    Returns: the total number of books on the cart at the start.
    """

    #: L1
    num_mystery_books = num_western_novels + num_biographies # eval: 11 = 5 + 6

    #: L2
    total_books = num_history_books + num_romance_books + num_poetry_books + num_mystery_books + num_western_novels + num_biographies # eval: 46 = 12 + 8 + 4 + 11 + 5 + 6

    #: FA
    answer = total_books
    return answer # eval: return 46
