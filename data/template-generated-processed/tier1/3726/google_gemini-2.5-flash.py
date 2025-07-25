def solve():
    """Index: 3726.
    Returns: the difference in the number of cans of cat food and dog food Chad bought.
    """
    # L1
    packages_cat_food = 6 # 6 packages of cat food
    cans_per_cat_package = 9 # Each package of cat food contained 9 cans
    total_cat_food_cans = packages_cat_food * cans_per_cat_package

    # L2
    packages_dog_food = 2 # 2 packages of dog food
    cans_per_dog_package = 3 # each package of dog food contained 3 cans
    total_dog_food_cans = packages_dog_food * cans_per_dog_package

    # L3
    difference_cans = total_cat_food_cans - total_dog_food_cans

    # FA
    answer = difference_cans
    return answer