def solve():
    """Index: 1653.
    Returns: the number of hours Beth will need to finish reading the remaining chapters.
    """
    # L1
    total_chapters = 8 # A book has 8 chapters
    chapters_read = 2 # Beth has read 2 chapters
    chapters_remaining = total_chapters - chapters_read

    # L2
    hours_spent = 3 # 3 hours
    chapters_per_hours = chapters_read # 2 chapters in 3 hours
    hours_per_chapter = hours_spent / chapters_per_hours

    # L3
    total_hours_remaining = hours_per_chapter * chapters_remaining

    # FA
    answer = total_hours_remaining
    return answer