def solve():
    """Index: 2184.
    Returns: the total number of pets Frankie has.
    """
    # L1
    four_legged_pets = 6 # Six of his pets have four legs
    dogs = 2 # He has 2 dogs
    cats = four_legged_pets - dogs

    # L2
    one_less_than_cats = 1 # one less parrot than cats
    parrots = cats - one_less_than_cats

    # L3
    six_more_than_cats = 6 # six more snakes than he has cats
    snakes = cats + six_more_than_cats

    # L4
    total_pets = dogs + cats + parrots + snakes

    # FA
    answer = total_pets
    return answer