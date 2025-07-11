def solve():
    """Index: 490.
    Returns: the length of the third side of the triangle.
    """
    # L1
    side1 = 40 # two of the sides are 40 cm
    side2 = 50 # two of the sides are 50 cm
    sum_first_two = side1 + side2

    # L2
    perimeter = 160 # The perimeter of a triangle is 160 cm
    third_side = perimeter - sum_first_two

    # FA
    answer = third_side
    return answer