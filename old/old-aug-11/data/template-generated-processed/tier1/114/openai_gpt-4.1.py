def solve():
    """Index: 114.
    Returns: the total number of pets Ed has.
    """
    # L1
    num_dogs = 2 # Ed has 2 dogs
    num_cats = 3 # 3 cats
    not_fish = num_dogs + num_cats

    # L2
    fish_multiplier = 2 # twice as many fish as cats and dogs combined
    num_fish = fish_multiplier * not_fish

    # L3
    total_pets = not_fish + num_fish

    # FA
    answer = total_pets
    return answer