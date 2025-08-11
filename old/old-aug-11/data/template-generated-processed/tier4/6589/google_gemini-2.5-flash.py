def solve():
    """Index: 6589.
    Returns: the number of books Billy reads.
    """
    # L1
    num_weekend_days = 2 # WK
    hours_per_day_weekend = 8 # 8 hours of free time on each day of the weekend
    total_free_hours_weekend = num_weekend_days * hours_per_day_weekend

    # L2
    total_percent = 100 # WK
    videogame_percent = 75 # 75% of his time playing video games
    reading_percent = total_percent - videogame_percent

    # L3
    reading_percent_decimal = 0.25 # the rest of his time reading (25%)
    reading_hours = total_free_hours_weekend * reading_percent_decimal

    # L4
    pages_per_hour = 60 # 60 pages an hour
    total_pages_read = reading_hours * pages_per_hour

    # L5
    pages_per_book = 80 # his books all contain 80 pages
    num_books_read = total_pages_read / pages_per_book

    # FA
    answer = num_books_read
    return answer