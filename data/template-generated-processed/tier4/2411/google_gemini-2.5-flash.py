def solve():
    """Index: 2411.
    Returns: the number of words Bo needs to learn per day.
    """
    # L1
    total_flashcards = 800 # 800 flashcards
    known_percent = 0.2 # knew 20% of the words
    known_words = total_flashcards * known_percent

    # L2
    words_to_learn = total_flashcards - known_words

    # L3
    days_to_learn = 40 # 40 days to learn the rest
    words_per_day = words_to_learn / days_to_learn

    # FA
    answer = words_per_day
    return answer