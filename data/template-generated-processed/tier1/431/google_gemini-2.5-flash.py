def solve():
    """Index: 431.
    Returns: the total number of legs in Javier's household.
    """
    # L1
    javier = 1 # Including Javier
    wife = 1 # a wife
    children = 3 # 3 children
    num_humans = javier + wife + children # Javier has a wife and 3 children. Including Javier
    legs_per_human = 2 # WK
    human_legs = num_humans * legs_per_human

    # L2
    num_dogs = 2 # 2 dogs
    num_cats = 1 # 1 cat
    num_four_legged_pets = num_dogs + num_cats

    # L3
    legs_per_four_legged_pet = 4 # WK
    pet_legs = num_four_legged_pets * legs_per_four_legged_pet

    # L4
    total_legs = human_legs + pet_legs

    # FA
    answer = total_legs
    return answer