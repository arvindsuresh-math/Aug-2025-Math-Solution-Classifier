from fractions import Fraction

def solve():
    """Index: 909.
    Returns: the total number of animals present in the compound.
    """
    # L1
    frogs = 160 # 160 frogs
    ratio_frogs_to_dogs = 2 # twice as many frogs as the number of dogs
    dogs = frogs / ratio_frogs_to_dogs

    # L2
    total_frogs_and_dogs = dogs + frogs

    # L3
    cat_percentage_less = Fraction(20, 100) # 20% less than the number of dogs
    cat_reduction_amount = cat_percentage_less * dogs

    # L4
    cats = dogs - cat_reduction_amount

    # L5
    total_animals = cats + total_frogs_and_dogs

    # FA
    answer = total_animals
    return answer