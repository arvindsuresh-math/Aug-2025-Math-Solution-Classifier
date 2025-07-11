from fractions import Fraction

def solve():
    """Index: 571.
    Returns: the total number of animals Anthony and Leonel have.
    """
    # L1
    anthony_total_pets = 12 # Anthony has 12 cats and dogs
    anthony_cat_fraction = Fraction(2, 3) # 2/3 of which are cats
    anthony_cats = anthony_cat_fraction * anthony_total_pets

    # L2
    anthony_dogs = anthony_total_pets - anthony_cats

    # L3
    leonel_cat_fraction = Fraction(1, 2) # half times as many cats as Anthony
    leonel_cats = leonel_cat_fraction * anthony_cats

    # L4
    leonel_additional_dogs = 7 # seven more dogs than Anthony
    leonel_dogs = anthony_dogs + leonel_additional_dogs

    # L5
    total_animals = leonel_dogs + leonel_cats + anthony_dogs + anthony_cats

    # FA
    answer = total_animals
    return answer