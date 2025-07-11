def solve():
    """Index: 1669.
    Returns: the number of goats in the field.
    """
    # L1
    sheep_and_goats_combined_count = 56 # 56 sheep and goats
    cows_count = 40 # 40 cows
    animals_excluding_goats = sheep_and_goats_combined_count + cows_count

    # L2
    total_animals_in_field = 200 # 200 animals
    number_of_goats = total_animals_in_field - animals_excluding_goats

    # FA
    answer = number_of_goats
    return answer