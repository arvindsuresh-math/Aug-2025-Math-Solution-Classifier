def solve():
    """Index: 4378.
    Returns: the total amount Rikki can expect to earn.
    """
    # L1
    hours_to_write = 2 # 2 hours to write poetry
    minutes_per_hour = 60 # WK
    total_writing_time_value = hours_to_write * minutes_per_hour

    # L2
    time_unit_minutes = 5 # 5 minutes
    num_five_minute_units = total_writing_time_value / time_unit_minutes

    # L3
    words_per_five_minutes = 25 # 25 words of poetry
    total_words_written = num_five_minute_units * words_per_five_minutes

    # L4
    price_per_word = 0.01 # $.01 a word
    total_earnings_dollars = total_words_written * price_per_word

    # FA
    answer = total_earnings_dollars
    return answer