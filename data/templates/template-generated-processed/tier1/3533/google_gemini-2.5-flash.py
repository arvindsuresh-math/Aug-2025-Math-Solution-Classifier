def solve():
    """Index: 3533.
    Returns: the length difference between the sides of square A and B.
    """
    # L3
    area_square_A = 25 # The area of square A is 25
    side_A = area_square_A ** 0.5

    # L5
    area_square_B = 81 # The area of square B is 81
    side_B = area_square_B ** 0.5

    # L6
    side_difference = side_B - side_A

    # FA
    answer = side_difference
    return answer