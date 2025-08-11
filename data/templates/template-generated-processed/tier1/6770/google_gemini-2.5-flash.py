def solve():
    """Index: 6770.
    Returns: the number of books currently in the library.
    """
    # L1
    books_bought_two_years_ago = 300 # bought 300 books
    more_books_last_year = 100 # bought 100 more books than she had bought the previous year
    books_bought_last_year = books_bought_two_years_ago + more_books_last_year

    # L2
    initial_books = 500 # 500 old books in the library
    total_books_as_of_last_year = initial_books + books_bought_two_years_ago + books_bought_last_year

    # L3
    books_donated_this_year = 200 # donated 200 of the library's old books
    current_books = total_books_as_of_last_year - books_donated_this_year

    # FA
    answer = current_books
    return answer