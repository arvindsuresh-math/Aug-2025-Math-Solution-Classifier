from fractions import Fraction

def solve():
    """Index: 1861.
    Returns: the total number of legs of dogs that are on the street.
    """
    # L1
    cat_fraction = Fraction(2, 3) # Two-thirds of all the animals
    total_animals = 300 # 300 animals on the street
    num_cats = cat_fraction * total_animals

    # L2
    num_dogs = total_animals - num_cats

    # L3
    legs_per_dog = 4 # WK
    total_dog_legs = num_dogs * legs_per_dog

    # FA
    answer = total_dog_legs
    return answer