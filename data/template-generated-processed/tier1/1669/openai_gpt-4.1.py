def solve():
    """Index: 1669.
    Returns: the number of goats in the field.
    """
    # L1
    sheep_and_goats = 56 # 56 sheep and goats
    cows = 40 # 40 cows
    animals_other_than_goats = sheep_and_goats + cows

    # L2
    total_animals = 200 # 200 animals
    goats = total_animals - animals_other_than_goats

    # FA
    answer = goats
    return answer