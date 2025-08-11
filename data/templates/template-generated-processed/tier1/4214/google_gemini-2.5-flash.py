def solve():
    """Index: 4214.
    Returns: the amount of money June spent on music books.
    """
    # L1
    num_maths_books = 4 # four maths books
    cost_maths_book = 20 # at $20 each
    cost_maths_books = num_maths_books * cost_maths_book

    # L2
    more_science_books = 6 # six more science books than maths books
    num_science_books = more_science_books + num_maths_books

    # L3
    cost_science_book = 10 # at $10 each
    cost_science_books = num_science_books * cost_science_book

    # L4
    multiplier_art_books = 2 # twice as many art books
    num_art_books = multiplier_art_books * num_maths_books

    # L5
    cost_art_book = 20 # at $20 each
    cost_art_books = num_art_books * cost_art_book

    # L6
    total_spent_other_books = cost_art_books + cost_science_books + cost_maths_books

    # L7
    initial_money = 500 # June has $500 for buying school supplies
    cost_music_books = initial_money - total_spent_other_books

    # FA
    answer = cost_music_books
    return answer