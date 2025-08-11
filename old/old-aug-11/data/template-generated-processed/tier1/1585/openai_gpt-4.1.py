def solve():
    """Index: 1585.
    Returns: the total number of shoes Olly needs for his pets.
    """
    # L2
    num_dogs = 3 # 3 dogs
    legs_per_animal = 4 # All the animals have 4 legs.
    dog_shoes = num_dogs * legs_per_animal

    # L3
    num_cats = 2 # 2 cats
    cat_shoes = num_cats * legs_per_animal

    # L4
    num_ferrets = 1 # a ferret
    ferret_shoes = num_ferrets * legs_per_animal

    # L5
    total_shoes = dog_shoes + cat_shoes + ferret_shoes

    # FA
    answer = total_shoes
    return answer