def solve():
    """Index: 1074.
    Returns: the square footage of the bathroom.
    """
    # L1
    num_tiles_width = 10 # 10 6 inch tiles along its width
    tile_length_inches = 6 # 6 inch tiles
    width_inches = num_tiles_width * tile_length_inches

    # L2
    inches_per_foot = 12 # WK
    width_feet = width_inches / inches_per_foot

    # L3
    num_tiles_length = 20 # 20 6 inch tiles along its length
    length_inches = num_tiles_length * tile_length_inches

    # L4
    length_feet = length_inches / inches_per_foot

    # L5
    square_footage = length_feet * width_feet

    # FA
    answer = square_footage
    return answer