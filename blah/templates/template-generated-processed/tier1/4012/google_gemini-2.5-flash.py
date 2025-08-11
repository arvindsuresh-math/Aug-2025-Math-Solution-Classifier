def solve():
    """Index: 4012.
    Returns: the total amount Michael has to pay.
    """
    # L1
    num_cats = 2 # 2 cats
    num_dogs = 3 # 3 dogs
    total_animals = num_cats + num_dogs

    # L2
    cost_per_animal_per_night = 13 # $13 a night per animal
    total_cost = total_animals * cost_per_animal_per_night

    # FA
    answer = total_cost
    return answer