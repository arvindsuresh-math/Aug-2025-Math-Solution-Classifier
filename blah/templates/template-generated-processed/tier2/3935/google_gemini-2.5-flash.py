def solve():
    """Index: 3935.
    Returns: the total number of pets after one month.
    """
    # L1
    initial_dogs = 30 # 30 dogs
    dog_adoption_percent_num = 50 # 50% of the dogs are adopted
    percent_to_decimal_factor = 0.01 # WK
    adopted_dogs = initial_dogs * dog_adoption_percent_num * percent_to_decimal_factor

    # L2
    initial_cats = 28 # 28 cats
    cat_adoption_percent_num = 25 # 25% of the cats are adopted
    adopted_cats = initial_cats * cat_adoption_percent_num * percent_to_decimal_factor

    # L3
    initial_lizards = 20 # 20 lizards
    lizard_adoption_percent_num = 20 # 20% of lizards are adopted
    adopted_lizards = initial_lizards * lizard_adoption_percent_num * percent_to_decimal_factor

    # L4
    initial_total_pets = initial_dogs + initial_cats + initial_lizards

    # L5
    pets_after_adoption = initial_total_pets - adopted_dogs - adopted_cats - adopted_lizards

    # L6
    new_pets_taken_in = 13 # 13 new pets a month
    final_total_pets = pets_after_adoption + new_pets_taken_in

    # FA
    answer = final_total_pets
    return answer