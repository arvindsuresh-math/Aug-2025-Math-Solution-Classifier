def solve():
    """Index: 5096.
    Returns: the total number of pages in the book.
    """
    # L1
    weeks_to_finish = 2 # 2 weeks for Sally to finish her book
    weekdays_per_week = 5 # WK
    total_weekdays = weekdays_per_week * weeks_to_finish

    # L2
    weekends_per_week = 2 # WK
    total_weekends = weekends_per_week * weeks_to_finish

    # L3
    pages_per_weekday = 10 # 10 pages of a book on weekdays
    pages_weekdays_total = pages_per_weekday * total_weekdays

    # L4
    pages_per_weekend = 20 # 20 pages on weekends
    pages_weekends_total = pages_per_weekend * total_weekends

    # L5
    total_pages = pages_weekdays_total + pages_weekends_total

    # FA
    answer = total_pages
    return answer