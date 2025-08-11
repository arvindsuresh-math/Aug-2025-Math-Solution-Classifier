def solve():
    """Index: 309.
    Returns: the number of words Carl can type in 7 days.
    """
    # L1
    carl_wpm = 50 # 50 words per minute
    minutes_per_hour = 60 # WK
    carl_wph = carl_wpm * minutes_per_hour

    # L2
    hours_per_day = 4 # 4 hours per day
    carl_per_day = carl_wph * hours_per_day

    # L3
    num_days = 7 # 7 days
    total_words = carl_per_day * num_days

    # FA
    answer = total_words
    return answer