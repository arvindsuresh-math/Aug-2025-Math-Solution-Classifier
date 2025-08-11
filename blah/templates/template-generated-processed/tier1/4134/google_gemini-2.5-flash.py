def solve():
    """Index: 4134.
    Returns: the length of the perimeter of the triangle.
    """
    # L2
    base = 4 # base of 4 inches
    base_squared = base * base

    # L3
    height = 3 # height of 3 inches
    height_squared = height * height

    # L4
    sum_of_squares = base_squared + height_squared

    # L5
    hypotenuse = sum_of_squares**0.5

    # L6
    base_plus_height = height + base

    # L7
    perimeter = base_plus_height + hypotenuse

    # FA
    answer = perimeter
    return answer