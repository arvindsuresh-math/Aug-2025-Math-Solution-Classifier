def solve():
    """Index: 1571.
    Returns: the number of 1-inch square tiles needed for the mosaic.
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

    # FA
    answer = total_area_sq_inches
    return answer