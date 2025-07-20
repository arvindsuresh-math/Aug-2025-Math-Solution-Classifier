def solve():
    """Index: 4711.
    Returns: the total hours Anna spends reading.
    """
    # L1
    total_chapters = 31 # 31-chapter textbook
    divisor = 3 # chapters that are divisible by 3
    chapters_divisible_by_3 = total_chapters // divisor

    # L2
    chapters_read = total_chapters - chapters_divisible_by_3

    # L3
    minutes_per_chapter = 20 # 20 minutes to read each chapter
    total_minutes_reading = chapters_read * minutes_per_chapter

    # L4
    minutes_per_hour = 60 # WK
    total_hours_reading = total_minutes_reading / minutes_per_hour

    # FA
    answer = total_hours_reading
    return answer