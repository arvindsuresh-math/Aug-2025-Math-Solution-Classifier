from fractions import Fraction

def solve():
    """Index: 667.
    Returns: the number of dogs with pointy ears.
    """
    # L1
    dogs_with_spots = 15 # If 15 dogs have spots
    double_factor = 2 # half the dogs have spots
    total_dogs = dogs_with_spots * double_factor

    # L2
    pointy_ears_fraction = Fraction(1, 5) # 1/5 have pointy ears
    dogs_with_pointy_ears = total_dogs * pointy_ears_fraction

    # FA
    answer = dogs_with_pointy_ears
    return answer