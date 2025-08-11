from fractions import Fraction

def solve():
    """Index: 1217.
    Returns: the total number of legs Camden's dogs have.
    """
    # L1
    justin_dogs = 14 # Justin has 14 dogs
    rico_more_dogs = 10 # 10 more dogs than Justin
    rico_dogs = justin_dogs + rico_more_dogs

    # L2
    camden_fraction = Fraction(3, 4) # 3/4 times as many dogs as Rico
    camden_dogs = camden_fraction * rico_dogs

    # L3
    legs_per_dog = 4 # A dog has four legs
    total_camden_dog_legs = camden_dogs * legs_per_dog

    # FA
    answer = total_camden_dog_legs
    return answer