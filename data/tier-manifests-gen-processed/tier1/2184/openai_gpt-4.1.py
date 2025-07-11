def solve():
    """Index: 2184.
    Returns: the total number of pets Frankie has.
    """
    # L1
    pets_with_four_legs = 6 # Six of his pets have four legs
    dogs = 2 # He has 2 dogs
    cats = pets_with_four_legs - dogs

    # L2
    parrots_less_than_cats = 1 # one less parrot than cats
    parrots = cats - parrots_less_than_cats

    # L3
    snakes_more_than_cats = 6 # six more snakes than he has cats
    snakes = cats + snakes_more_than_cats

    # L4
    total_pets = dogs + cats + parrots + snakes

    # FA
    answer = total_pets
    return answer