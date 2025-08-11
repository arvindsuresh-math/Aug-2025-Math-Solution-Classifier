def solve():
    """Index: 710.
    Returns: the number of pieces of candy left.
    """
    # L1
    pieces_eaten_each = 4 # Each of them ate 4 pieces of candy
    num_people = 2 # Travis and his brother
    total_eaten = pieces_eaten_each * num_people

    # L2
    total_collected = 68 # collected 68 pieces of candy altogether
    candy_left = total_collected - total_eaten

    # FA
    answer = candy_left
    return answer