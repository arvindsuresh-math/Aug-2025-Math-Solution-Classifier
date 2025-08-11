def solve():
    """Index: 7318.
    Returns: how many more orange pages Mirella read than purple pages.
    """
    # L1
    num_purple_books = 5 # read 5 purple books
    pages_per_purple_book = 230 # Each purple book has 230 pages
    total_purple_pages = num_purple_books * pages_per_purple_book

    # L2
    num_orange_books = 4 # read 4 orange books
    pages_per_orange_book = 510 # Each orange book contains 510 pages
    total_orange_pages = num_orange_books * pages_per_orange_book

    # L3
    difference_pages = total_orange_pages - total_purple_pages

    # FA
    answer = difference_pages
    return answer