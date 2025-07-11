def solve():
    """Index: 2411.
    Returns: the number of words Bo needs to learn per day.
    """
    # L1
    total_flashcards = 800 # 800 flashcards
    known_percent = 0.2 # 20% of the words on them
    known_words = total_flashcards * known_percent

    # L2
    words_to_learn = total_flashcards - known_words

    # L3
    days = 40 # 40 days to learn the rest
    words_per_day = words_to_learn / days

    # FA
    answer = words_per_day
    return answer