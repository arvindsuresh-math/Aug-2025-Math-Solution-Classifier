def solve():
    """Index: 3730.
    Returns: the time Kristin will take to read half of her books.
    """
    # L1
    peter_read_time_per_book = 18 # Peter reads one book in 18 hours
    speed_multiplier = 3 # Peter can read three times as fast as Kristin
    kristin_time_per_book = peter_read_time_per_book * speed_multiplier

    # L2
    total_books_kristin = 20 # Kristin are to read 20 fantasy novels each
    half_divisor = 2 # half of her books
    kristin_books_to_read = total_books_kristin / half_divisor

    # L3
    total_time_kristin = kristin_books_to_read * kristin_time_per_book

    # FA
    answer = total_time_kristin
    return answer