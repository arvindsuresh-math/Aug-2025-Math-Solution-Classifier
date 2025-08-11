def solve():
    """Index: 7447.
    Returns: the total number of animals in the shelter.
    """
    # L1
    initial_cats = 15 # 15 cats in a shelter
    adopted_divisor = 3 # One-third were adopted
    adopted_cats = initial_cats / adopted_divisor

    # L2
    cats_left_after_adoption = initial_cats - adopted_cats

    # L3
    replacement_multiplier = 2 # twice the amount that were adopted
    added_cats = adopted_cats * replacement_multiplier

    # L4
    total_cats = cats_left_after_adoption + added_cats

    # L5
    dogs_multiplier = 2 # twice as many dogs showed up as there are cats
    total_dogs = total_cats * dogs_multiplier

    # L6
    total_animals = total_cats + total_dogs

    # FA
    answer = total_animals
    return answer