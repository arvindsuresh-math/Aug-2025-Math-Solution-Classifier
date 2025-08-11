def solve():
    """Index: 3565.
    Returns: the length of the patio in feet.
    """
    # L5
    perimeter = 100 # perimeter of the patio was 100 feet
    # The problem states the length is four times the width. For a rectangle, the perimeter is 2*(width + length).
    # If width = x and length = 4x, then perimeter = 2*(x + 4x) = 2*(5x) = 10x.
    # The coefficient '10' is derived from this relationship and the perimeter formula.
    perimeter_equation_coefficient = 10 # derived from the relationship between length and width in the perimeter formula
    width = perimeter / perimeter_equation_coefficient

    # L6
    length_multiplier = 4 # four times as long as it was wide
    length = length_multiplier * width

    # FA
    answer = length
    return answer