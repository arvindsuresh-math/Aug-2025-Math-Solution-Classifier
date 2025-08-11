def solve():
    """Index: 5965.
    Returns: the total number of legs his animals have.
    """
    # L1
    num_horses = 2 # 2 horses
    num_dogs = 5 # 5 dogs
    num_cats = 7 # 7 cats
    num_turtles = 3 # 3 turtles
    num_goat = 1 # 1 goat
    total_animals = num_horses + num_dogs + num_cats + num_turtles + num_goat

    # L2
    legs_per_animal = 4 # WK
    total_legs = total_animals * legs_per_animal

    # FA
    answer = total_legs
    return answer