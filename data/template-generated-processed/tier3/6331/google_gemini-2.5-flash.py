def solve():
    """Index: 6331.
    Returns: the time it takes Brianna to read the book in minutes.
    """
    # L1
    anna_pages_per_minute = 1 # 1 page in 1 minute
    anna_minutes_per_page = 1 # 1 page in 1 minute
    anna_speed = anna_pages_per_minute / anna_minutes_per_page

    # L2
    carole_speed = anna_speed

    # L3
    brianna_speed_multiplier = 2 # WK
    brianna_speed = brianna_speed_multiplier * carole_speed

    # L4
    book_pages = 100 # a 100-page book
    time_to_read_book = book_pages / brianna_speed

    # FA
    answer = time_to_read_book
    return answer