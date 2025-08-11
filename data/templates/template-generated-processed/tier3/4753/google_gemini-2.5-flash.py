def solve():
    """Index: 4753.
    Returns: the number of bushes Alice needs to buy.
    """
    # L1
    side_length = 16 # each side is 16 feet long
    num_sides = 3 # three sides of her yard
    total_distance = side_length * num_sides

    # L2
    bush_fill_distance = 4 # each bush fills 4 feet
    num_bushes = total_distance / bush_fill_distance

    # FA
    answer = num_bushes
    return answer