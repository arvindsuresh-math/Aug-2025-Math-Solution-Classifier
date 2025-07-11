def solve():
    """Index: 1392.
    Returns: the total number of weeks it took Cody to read his series.
    """
    # L1
    total_books = 54 # The series was 54 books in total
    first_week_books = 6 # read 6 books the first week
    second_week_books = 3 # and 3 books the second week
    remaining_books_after_initial_weeks = total_books - first_week_books - second_week_books

    # L2
    books_per_week_after = 9 # then 9 books every week after that
    weeks_for_remaining_books = remaining_books_after_initial_weeks / books_per_week_after

    # L3
    first_initial_week = 1 # WK
    second_initial_week = 1 # WK
    total_weeks = first_initial_week + second_initial_week + weeks_for_remaining_books

    # FA
    answer = total_weeks
    return answer