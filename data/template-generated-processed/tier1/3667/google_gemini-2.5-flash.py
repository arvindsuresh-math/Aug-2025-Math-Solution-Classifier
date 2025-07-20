def solve():
    """Index: 3667.
    Returns: the number of pages Juwella will read tonight.
    """
    # L1
    pages_three_nights_ago = 15 # read 15 pages
    multiplier_twice = 2 # twice that many pages
    pages_two_nights_ago = pages_three_nights_ago * multiplier_twice

    # L2
    pages_more_last_night = 5 # 5 pages more than the previous night
    pages_last_night = pages_two_nights_ago + pages_more_last_night

    # L3
    total_pages_read = pages_three_nights_ago + pages_two_nights_ago + pages_last_night

    # L4
    total_book_pages = 100 # book has 100 pages
    pages_to_read_tonight = total_book_pages - total_pages_read

    # FA
    answer = pages_to_read_tonight
    return answer