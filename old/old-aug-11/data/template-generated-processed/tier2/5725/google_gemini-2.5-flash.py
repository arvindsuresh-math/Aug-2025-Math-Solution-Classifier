def solve():
    """Index: 5725.
    Returns: the number of words Tim knew originally.
    """
    # L1
    years = 2 # In 2 years
    days_per_year = 365 # WK
    total_days = days_per_year * years

    # L2
    words_per_day = 10 # learns 10 words from it a day
    words_learned = total_days * words_per_day

    # L3
    increase_decimal = 0.5 # by 50%
    one_for_ratio = 1 # WK
    ratio_to_original = one_for_ratio / increase_decimal

    # L4
    original_words = words_learned * ratio_to_original

    # FA
    answer = original_words
    return answer