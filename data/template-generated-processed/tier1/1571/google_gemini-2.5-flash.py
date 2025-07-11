def solve():
    """Index: 1571.
    Returns: the total number of tiles needed for the mosaic.
    """
    # L1
    mural_length_feet = 15 # 15 feet long
    inches_per_foot = 12 # WK
    mural_length_inches = mural_length_feet * inches_per_foot

    # L2
    mural_height_feet = 10 # 10 feet tall
    mural_height_inches = mural_height_feet * inches_per_foot

    # L3
    total_area_sq_inches = mural_length_inches * mural_height_inches
    num_tiles = total_area_sq_inches # Since each tile is 1 square inch, this is also the number of tiles she needs.

    # FA
    answer = num_tiles
    return answer