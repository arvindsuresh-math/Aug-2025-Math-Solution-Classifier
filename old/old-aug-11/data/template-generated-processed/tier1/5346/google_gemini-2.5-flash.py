def solve():
    """Index: 5346.
    Returns: the number of books Henry now has.
    """
    # L1
    num_boxes = 3 # 3 boxes
    books_per_box = 15 # 15 books each
    books_from_boxes = num_boxes * books_per_box

    # L2
    books_in_room = 21 # 21 books in a room
    books_coffee_table = 4 # 4 on his coffee table
    cookbooks_kitchen = 18 # 18 cookbooks stashed in the kitchen
    total_donated_books = books_from_boxes + books_in_room + books_coffee_table + cookbooks_kitchen

    # L3
    initial_collection = 99 # book collection of 99 books
    books_remaining_after_donation = initial_collection - total_donated_books

    # L4
    books_picked_up = 12 # grabbed 12 books
    final_books = books_picked_up + books_remaining_after_donation

    # FA
    answer = final_books
    return answer