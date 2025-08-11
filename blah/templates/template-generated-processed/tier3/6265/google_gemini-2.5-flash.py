def solve():
    """Index: 6265.
    Returns: the length of one side of the square patch of land.
    """
    # L1
    length_rectangle = 400 # length of 400 feet
    width_rectangle = 300 # width of 300 feet
    sides_multiplier = 2 # WK
    product_length = sides_multiplier * length_rectangle
    product_width = sides_multiplier * width_rectangle
    perimeter_rectangle = product_length + product_width

    # L2
    double_multiplier = 2 # twice as large
    perimeter_square = perimeter_rectangle * double_multiplier

    # L3
    sides_square = 4 # WK
    side_length_square = perimeter_square / sides_square

    # FA
    answer = side_length_square
    return answer