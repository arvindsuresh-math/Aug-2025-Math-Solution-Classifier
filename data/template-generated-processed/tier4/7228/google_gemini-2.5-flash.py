def solve():
    """Index: 7228.
    Returns: the total number of books Pete read across both years.
    """
    # L1
    matt_second_year_books = 75 # Matt read 75 books in his second year
    matt_increase_factor = 1.5 # Matt reads only 50% more
    matt_first_year_books = matt_second_year_books / matt_increase_factor

    # L2
    pete_first_year_multiplier = 2 # Pete read twice as many books as Matt did last year
    pete_first_year_books = matt_first_year_books * pete_first_year_multiplier

    # L3
    pete_second_year_multiplier = 2 # he doubles that number
    pete_second_year_books = pete_first_year_books * pete_second_year_multiplier

    # L4
    total_pete_books = pete_second_year_books + pete_first_year_books

    # FA
    answer = total_pete_books
    return answer