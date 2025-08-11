def solve():
    """Index: 5612.
    Returns: the total number of movies and books Sue now has.
    """
    # L1
    initial_books = 15 # borrowed 15 books
    returned_books = 8 # returned 8 books
    books_after_returning = initial_books - returned_books

    # L2
    initial_movies = 6 # 6 movies
    returned_movies_divisor = 3 # a third of the movies
    movies_returned = initial_movies / returned_movies_divisor

    # L3
    movies_left = initial_movies - movies_returned

    # L4
    checked_out_books = 9 # checked out 9 more books
    total_books = books_after_returning + checked_out_books

    # L5
    total_items = total_books + movies_left

    # FA
    answer = total_items
    return answer