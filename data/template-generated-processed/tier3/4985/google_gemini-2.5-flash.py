from fractions import Fraction

def solve():
    """Index: 4985.
    Returns: the area of the smaller rectangle.
    """
    # L1
    half_factor = Fraction(1, 2) # half the length and width
    big_rectangle_length = 40 # length of 40 meters
    small_rectangle_length = half_factor * big_rectangle_length

    # L2
    big_rectangle_width = 20 # width of 20 meters
    small_rectangle_width = half_factor * big_rectangle_width

    # L3
    small_rectangle_area = small_rectangle_length * small_rectangle_width

    # FA
    answer = small_rectangle_area
    return answer