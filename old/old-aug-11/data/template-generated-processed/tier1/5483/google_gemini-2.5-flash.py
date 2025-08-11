def solve():
    """Index: 5483.
    Returns: the total distance Karen covers.
    """
    # L1
    books_per_shelf = 400 # 400 books each
    num_shelves = 4 # four shelves
    total_books = num_shelves * books_per_shelf

    # L2
    distance_one_way = total_books # The total number of books on four shelves ... is the same as the distance in miles that Karen bikes back to her home from the library
    total_distance = distance_one_way + distance_one_way

    # FA
    answer = total_distance
    return answer