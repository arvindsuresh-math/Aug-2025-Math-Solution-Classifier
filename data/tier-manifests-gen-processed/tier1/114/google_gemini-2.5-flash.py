def solve():
    """Index: 114.
    Returns: the total number of pets Ed has.
    """
    # L1
    dogs = 2 # 2 dogs
    cats = 3 # 3 cats
    non_fish_pets = dogs + cats

    # L2
    multiplier_for_fish = 2 # twice as many fish
    fish = multiplier_for_fish * non_fish_pets

    # L3
    total_pets = non_fish_pets + fish

    # FA
    answer = total_pets
    return answer