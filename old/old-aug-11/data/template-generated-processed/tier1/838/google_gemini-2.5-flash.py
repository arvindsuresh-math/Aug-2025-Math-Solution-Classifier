def solve():
    """Index: 838.
    Returns: the total number of animals that made it to the shore.
    """
    # L1
    initial_sheep = 20 # 20 sheep
    sheep_drowned = 3 # 3 of the sheep drowned
    sheep_made_it = initial_sheep - sheep_drowned

    # L2
    multiplier_cows_drowned = 2 # Twice as many cows drowned as did sheep
    cows_drowned = multiplier_cows_drowned * sheep_drowned

    # L3
    initial_cows = 10 # 10 cows
    cows_made_it = initial_cows - cows_drowned

    # L4
    initial_dogs = 14 # 14 dogs
    total_animals_made_it = sheep_made_it + cows_made_it + initial_dogs

    # FA
    answer = total_animals_made_it
    return answer