def solve():
    """Index: 639.
    Returns: the total number of dogs and cats in the community.
    """
    # L1
    families_with_2_dogs = 15 # 15 families own 2 dogs
    dogs_per_family_2 = 2 # 2 dogs
    dogs_from_2dog_families = families_with_2_dogs * dogs_per_family_2

    # L2
    families_with_1_dog = 20 # 20 families own 1 dog
    dogs_per_family_1 = 1 # 1 dog
    dogs_from_1dog_families = families_with_1_dog * dogs_per_family_1

    # L3
    total_families = 50 # 50 families
    cat_owner_families = total_families - families_with_2_dogs - families_with_1_dog

    # L4
    cats_per_family = 2 # 2 cats each
    cats_from_cat_families = cat_owner_families * cats_per_family

    # L5
    total_pets = dogs_from_2dog_families + dogs_from_1dog_families + cats_from_cat_families

    # FA
    answer = total_pets
    return answer