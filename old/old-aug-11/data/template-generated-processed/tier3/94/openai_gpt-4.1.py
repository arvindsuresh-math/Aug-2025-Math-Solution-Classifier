def solve():
    """Index: 94.
    Returns: the number of days it will take John to write 3 books of 400 pages each at 20 pages per day.
    """
    # L1
    num_books = 3 # 3 books
    pages_per_book = 400 # 400 pages each
    total_pages = num_books * pages_per_book

    # L2
    pages_per_day = 20 # John writes 20 pages a day
    days_needed = total_pages / pages_per_day

    # FA
    answer = days_needed
    return answer