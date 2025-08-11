def solve():
    """Index: 4453.
    Returns: how many pounds over the bookcase's weight limit the collection is.
    """
    # L1
    num_hardcover_books = 70 # 70 hardcover books
    weight_hardcover_book = 0.5 # half a pound
    total_weight_hardcover = num_hardcover_books * weight_hardcover_book

    # L2
    num_textbooks = 30 # 30 textbooks
    weight_textbook = 2 # 2 pounds
    total_weight_textbooks = num_textbooks * weight_textbook

    # L3
    num_knick_knacks = 3 # 3 knick-knacks
    weight_knick_knack = 6 # 6 pounds
    total_weight_knick_knacks = num_knick_knacks * weight_knick_knack

    # L4
    total_collection_weight = total_weight_hardcover + total_weight_textbooks + total_weight_knick_knacks

    # L5
    bookcase_weight_limit = 80 # maximum of 80 pounds of weight
    over_limit_pounds = total_collection_weight - bookcase_weight_limit

    # FA
    answer = over_limit_pounds
    return answer