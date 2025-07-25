def solve():
    """Index: 5930.
    Returns: the total amount of cleaner needed.
    """
    # L1
    cleaner_per_dog = 6 # 6 ounces of pet cleaner to clean up a dog stain
    num_dogs = 6 # 6 dogs
    total_cleaner_dogs = cleaner_per_dog * num_dogs

    # L2
    cleaner_per_cat = 4 # 4 ounces to clean up a cat stain
    num_cats = 3 # 3 cats
    total_cleaner_cats = cleaner_per_cat * num_cats

    # L3
    cleaner_per_rabbit = 1 # 1 ounce to clean up a rabbit stain
    num_rabbits = 1 # 1 rabbit
    total_cleaner_rabbit = cleaner_per_rabbit * num_rabbits
    total_cleaner_all_species = total_cleaner_dogs + total_cleaner_cats + total_cleaner_rabbit

    # FA
    answer = total_cleaner_all_species
    return answer