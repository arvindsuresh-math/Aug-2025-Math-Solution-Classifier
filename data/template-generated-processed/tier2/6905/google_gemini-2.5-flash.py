def solve():
    """Index: 6905.
    Returns: the difference in the number of books Peter has read compared to his brother.
    """
    # L1
    total_books = 20 # Peter has 20 books
    peter_read_percent_decimal = 0.4 # read 40% of them
    peter_books_read = total_books * peter_read_percent_decimal

    # L2
    brother_read_percent_decimal = 0.1 # brother has read 10% of them
    brother_books_read = total_books * brother_read_percent_decimal

    # L3
    difference_in_books_read = peter_books_read - brother_books_read

    # FA
    answer = difference_in_books_read
    return answer