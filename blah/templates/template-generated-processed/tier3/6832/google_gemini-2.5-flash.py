def solve():
    """Index: 6832.
    Returns: the number of pages Juan reads in an hour.
    """
    # L1
    time_to_lunch_one_way = 4 # 4 hours to move from his office to grab lunch
    round_trip_multiplier = 2 # back takes 2*4
    time_to_lunch_round_trip = round_trip_multiplier * time_to_lunch_one_way

    # L2
    book_reading_multiplier = 2 # half the time he takes to read a book
    time_to_read_book = time_to_lunch_round_trip * book_reading_multiplier

    # L3
    total_pages_in_book = 4000 # 4000-page book
    pages_per_hour = total_pages_in_book / time_to_read_book

    # FA
    answer = pages_per_hour
    return answer