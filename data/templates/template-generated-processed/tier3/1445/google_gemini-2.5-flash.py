def solve():
    """Index: 1445.
    Returns: the average number of minutes per day Jenny should spend reading.
    """
    # L1
    first_book_words = 200 # the first book has 200 words
    second_book_words = 400 # the second book has 400 words
    third_book_words = 300 # and the third book has 300 words
    total_words = first_book_words + second_book_words + third_book_words

    # L2
    reading_speed_words_per_hour = 100 # She can read 100 words per hour
    total_hours_reading = total_words / reading_speed_words_per_hour

    # L3
    minutes_per_hour = 60 # WK
    total_minutes_reading = total_hours_reading * minutes_per_hour

    # L4
    total_days = 10 # in the next 10 days
    minutes_per_day_average = total_minutes_reading / total_days

    # FA
    answer = minutes_per_day_average
    return answer