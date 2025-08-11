from fractions import Fraction

def solve():
    """Index: 4290.
    Returns: the number of additional centimeters Mary needs to grow.
    """
    # L1
    brother_height = 180 # Mary's brother is 180 cm
    mary_height_fraction = Fraction(2, 3) # Mary is 2/3 the height of her brother
    mary_current_height = brother_height * mary_height_fraction

    # L2
    min_height = 140 # The minimum height to ride the roller coaster is 140 cm
    height_needed = min_height - mary_current_height

    # FA
    answer = height_needed
    return answer