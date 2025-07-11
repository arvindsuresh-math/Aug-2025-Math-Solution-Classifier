def solve():
    """Index: 2386.
    Returns: the total number of cats the shelter has now.
    """
    # L1
    newly_taken_in_cats = 12 # recently took in twelve cats
    initial_half_divisor = 2 # half that number of cats
    initial_cats = newly_taken_in_cats / initial_half_divisor

    # L2
    cats_after_intake = newly_taken_in_cats + initial_cats

    # L3
    adopted_cats = 3 # three had been adopted
    cats_after_adoption = cats_after_intake - adopted_cats

    # L4
    kittens = 5 # one of the cats had five kittens
    cats_after_kittens = cats_after_adoption + kittens

    # L5
    missing_pet_returned = 1 # one person arrived to pick up one of the cats
    final_cats = cats_after_kittens - missing_pet_returned

    # FA
    answer = final_cats
    return answer