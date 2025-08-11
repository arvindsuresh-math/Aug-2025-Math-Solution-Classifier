def solve():
    """Index: 1199.
    Returns: the number of bookshelves Jonas can put in the room.
    """
    # L1
    total_room_space = 400 # This room has 400 square feet of space
    reserved_space = 160 # If he reserves 160 square feet of space
    remaining_space = total_room_space - reserved_space

    # L2
    space_per_bookshelf = 80 # each bookshelf takes up 80 square feet of space
    num_bookshelves = remaining_space / space_per_bookshelf

    # FA
    answer = num_bookshelves
    return answer