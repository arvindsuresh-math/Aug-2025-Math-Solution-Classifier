def solve():
    """Index: 5646.
    Returns: the number of weeks it takes to read the book.
    """
    # L1
    pages_per_day_read = 100 # He reads 100 pages Monday, Wed, and Friday
    reading_days_per_week = 3 # Monday, Wed, and Friday
    pages_per_week = pages_per_day_read * reading_days_per_week

    # L2
    total_pages = 2100 # The book is 2100 pages long
    weeks_to_read = total_pages / pages_per_week

    # FA
    answer = weeks_to_read
    return answer