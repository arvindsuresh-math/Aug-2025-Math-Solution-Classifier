def solve():
    """Index: 5370.
    Returns: the number of 6-inch pencils that can be placed across the diameter of the circle.
    """
    # L1
    radius = 14 # radius of 14 feet
    diameter_factor = 2 # WK
    diameter_feet = diameter_factor * radius

    # L2
    pencil_length_inches = 6 # 6-inch pencils
    inches_per_foot = 12 # WK
    pencil_length_feet = pencil_length_inches / inches_per_foot

    # L3
    num_pencils = diameter_feet / pencil_length_feet

    # FA
    answer = num_pencils
    return answer