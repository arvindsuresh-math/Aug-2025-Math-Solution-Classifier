def solve():
    """Index: 431.
    Returns: the total number of legs in Javier’s household.
    """
    # L1
    num_humans = 1 + 1 + 3 # Javier has a wife and 3 children (including Javier)
    legs_per_human = 2 # WK
    human_legs = num_humans * legs_per_human

    # L2
    num_dogs = 2 # 2 dogs
    num_cats = 1 # 1 cat
    num_pets = num_dogs + num_cats

    # L3
    legs_per_pet = 4 # WK
    pet_legs = num_pets * legs_per_pet

    # L4
    total_legs = human_legs + pet_legs

    # FA
    answer = total_legs
    return answer