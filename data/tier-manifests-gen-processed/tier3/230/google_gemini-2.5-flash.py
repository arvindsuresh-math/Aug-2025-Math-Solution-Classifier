def solve():
    """Index: 230.
    Returns: the average number of days the two take to read the book.
    """
    # L1
    emery_days = 20 # 20 days to read
    reading_speed_factor = 5 # five times as fast
    serena_days = reading_speed_factor * emery_days

    # L2
    total_days_taken = serena_days + emery_days

    # L3
    number_of_readers = 2 # the two
    average_days = total_days_taken / number_of_readers

    # FA
    answer = average_days
    return answer