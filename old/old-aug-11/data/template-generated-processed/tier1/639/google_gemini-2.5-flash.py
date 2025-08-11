def solve():
    """Index: 639.
    Returns: the total number of dogs and cats in the community.
    """
    # L1
    families_2_dogs = 15 # 15 families own 2 dogs
    dogs_per_family_2_dogs = 2 # 2 dogs
    dogs_from_2_dog_families = families_2_dogs * dogs_per_family_2_dogs

    # L2
    families_1_dog = 20 # 20 families own 1 dog
    dogs_per_family_1_dog = 1 # 1 dog
    dogs_from_1_dog_families = families_1_dog * dogs_per_family_1_dog

    # L3
    total_families = 50 # 50 families
    cat_owners = total_families - families_2_dogs - families_1_dog

    # L4
    cats_per_family_remaining = 2 # 2 cats each
    total_cats = cat_owners * cats_per_family_remaining

    # L5
    total_animals = dogs_from_2_dog_families + dogs_from_1_dog_families + total_cats

    # FA
    answer = total_animals
    return answer