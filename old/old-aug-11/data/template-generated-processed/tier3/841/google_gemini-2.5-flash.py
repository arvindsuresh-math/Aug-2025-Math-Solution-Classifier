from fractions import Fraction

def solve():
    """Index: 841.
    Returns: the number of dogs Heloise remains with.
    """
    # L1
    dog_ratio_part = 10 # ratio of 10:17
    cat_ratio_part = 17 # ratio of 10:17
    total_ratio_parts = dog_ratio_part + cat_ratio_part

    # L2
    total_pets = 189 # total number of pets being 189
    dog_fraction = Fraction(dog_ratio_part, total_ratio_parts)
    initial_dogs = dog_fraction * total_pets

    # L3
    dogs_given_away = 10 # gives 10 dogs
    remaining_dogs = initial_dogs - dogs_given_away

    # FA
    answer = remaining_dogs
    return answer