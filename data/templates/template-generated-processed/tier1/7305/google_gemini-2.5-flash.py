def solve():
    """Index: 7305.
    Returns: the original number of cats in the neighborhood.
    """
    # L1
    current_cats = 20 # 20 cats now
    multiplier_twice = 2 # twice as many dogs as cats
    current_dogs = multiplier_twice * current_cats

    # L2
    new_dogs_born = 20 # twenty new dogs were born
    original_dogs = current_dogs - new_dogs_born

    # L3
    factor_for_original_cats = 2 # half the number of cats (implies original_cats = original_dogs * 2)
    original_cats = original_dogs * factor_for_original_cats

    # FA
    answer = original_cats
    return answer