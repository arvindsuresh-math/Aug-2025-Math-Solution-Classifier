def solve():
    """Index: 6498.
    Returns: the average number of pages the second person read each day of break.
    """
    # L1
    deshaun_books_read = 60 # 60 books over the summer
    avg_pages_per_book = 320 # 320 pages long
    deshaun_total_pages = deshaun_books_read * avg_pages_per_book

    # L2
    second_person_read_factor = 0.75 # 75% as much as he did
    second_person_total_pages = deshaun_total_pages * second_person_read_factor

    # L3
    summer_break_days = 80 # Summer break is 80 days long
    second_person_avg_pages_per_day = second_person_total_pages / summer_break_days

    # FA
    answer = second_person_avg_pages_per_day
    return answer