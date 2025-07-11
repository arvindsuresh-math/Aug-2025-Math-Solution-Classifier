def solve():
    """Index: 490.
    Returns: the length of the third side of the triangle.
    """
    # L1
    side1 = 40 # 40 cm
    side2 = 50 # 50 cm
    sum_of_two_sides = side1 + side2

    # L2
    perimeter = 160 # 160 cm
    third_side = perimeter - sum_of_two_sides

    # FA
    answer = third_side
    return answer