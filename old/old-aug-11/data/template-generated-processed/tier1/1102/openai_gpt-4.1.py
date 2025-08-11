def solve():
    """Index: 1102.
    Returns: the number of times Carla counted something on Tuesday.
    """
    # L1
    num_tiles = 38 # counts the tiles on the ceiling--38
    tile_counts_tuesday = 2 # counts all the tiles twice in a row
    tile_counted_times = num_tiles * tile_counts_tuesday

    # L2
    num_books = 75 # counts the books in the room--75
    book_counts_tuesday = 3 # counts the books three times in a row
    book_counted_times = num_books * book_counts_tuesday

    # L3
    total_counted_tuesday = tile_counted_times + book_counted_times

    # FA
    answer = total_counted_tuesday
    return answer