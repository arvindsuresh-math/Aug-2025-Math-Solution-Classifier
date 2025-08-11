def solve():
    """Index: 1585.
    Returns: the total number of shoes Olly needs for his pets.
    """
    # L2
    num_dogs = 3 # 3 dogs
    legs_per_animal = 4 # WK
    shoes_for_dogs = num_dogs * legs_per_animal

    # L3
    num_cats = 2 # 2 cats
    shoes_for_cats = num_cats * legs_per_animal

    # L4
    num_ferrets = 1 # a ferret
    shoes_for_ferret = num_ferrets * legs_per_animal

    # L5
    total_shoes = shoes_for_dogs + shoes_for_cats + shoes_for_ferret

    # FA
    answer = total_shoes
    return answer