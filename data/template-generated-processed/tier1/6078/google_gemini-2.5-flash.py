def solve():
    """Index: 6078.
    Returns: the number of pages Cyrus still needs to write.
    """
    # L1
    first_day_pages = 25 # writes 25 pages
    multiplier_twice = 2 # twice that amount
    second_day_pages = multiplier_twice * first_day_pages

    # L2
    third_day_pages = multiplier_twice * second_day_pages

    # L3
    fourth_day_pages = 10 # only able to write 10 pages
    total_pages_written = first_day_pages + second_day_pages + third_day_pages + fourth_day_pages

    # L4
    total_book_pages = 500 # write a 500 page book
    pages_remaining = total_book_pages - total_pages_written

    # FA
    answer = pages_remaining
    return answer