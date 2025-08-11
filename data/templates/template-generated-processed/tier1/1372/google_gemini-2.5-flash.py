def solve():
    """Index: 1372.
    Returns: how many more words Isaiah can type than Micah in an hour.
    """
    # L2
    micah_wpm = 20 # 20 words per minute
    minutes_per_hour = 60 # WK
    micah_wph = micah_wpm * minutes_per_hour

    # L3
    isaiah_wpm = 40 # 40 words per minute
    isaiah_wph = isaiah_wpm * minutes_per_hour

    # L4
    difference_in_words = isaiah_wph - micah_wph

    # FA
    answer = difference_in_words
    return answer