def solve():
    """Index: 503.
    Returns: the number of pages Yasna needs to read every day to finish both books in two weeks.
    """
    # L1
    book1_pages = 180 # One book is 180 pages long
    book2_pages = 100 # the other book is 100 pages long
    total_pages = book1_pages + book2_pages

    # L2
    days_in_two_weeks = 14 # two weeks
    pages_per_day = total_pages / days_in_two_weeks

    # FA
    answer = pages_per_day
    return answer