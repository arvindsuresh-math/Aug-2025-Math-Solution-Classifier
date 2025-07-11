def solve():
    """Index: 230.
    Returns: the average number of days Emery and Serena take to read the book.
    """
    # L1
    emery_days = 20 # the book takes her 20 days to read
    serena_speed_factor = 5 # Emery can read five times as fast as Serena
    serena_days = serena_speed_factor * emery_days

    # L2
    total_days = serena_days + emery_days

    # L3
    num_people = 2 # WK
    average_days = total_days / num_people

    # FA
    answer = average_days
    return answer