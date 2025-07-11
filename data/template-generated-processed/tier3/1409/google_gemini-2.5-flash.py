def solve():
    """Index: 1409.
    Returns: the total number of free donuts Quinn is eligible for.
    """
    # L1
    books_per_week = 2 # read 2 books a week
    total_weeks = 10 # for 10 weeks total
    total_books_read = books_per_week * total_weeks

    # L2
    books_per_donut = 5 # For every 5 books you read
    free_donuts = total_books_read / books_per_donut

    # FA
    answer = free_donuts
    return answer