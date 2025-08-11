def solve():
    """Index: 1102.
    Returns: the total number of times Carla counted something on Tuesday.
    """
    # L1
    ceiling_tiles_monday = 38 # counts the tiles on the ceiling--38
    times_counted_tiles_tuesday = 2 # counted all the tiles twice in a row
    tiles_counted_tuesday = ceiling_tiles_monday * times_counted_tiles_tuesday

    # L2
    books_monday = 75 # counts the books in the room--75
    times_counted_books_tuesday = 3 # counts the books three times in a row
    books_counted_tuesday = books_monday * times_counted_books_tuesday

    # L3
    total_counts_tuesday = tiles_counted_tuesday + books_counted_tuesday

    # FA
    answer = total_counts_tuesday
    return answer