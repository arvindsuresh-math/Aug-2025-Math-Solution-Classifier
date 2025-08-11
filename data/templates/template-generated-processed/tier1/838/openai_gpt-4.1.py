def solve():
    """Index: 838.
    Returns: the total number of animals that made it to the shore.
    """
    # L1
    total_sheep = 20 # 20 sheep
    sheep_drowned = 3 # 3 of the sheep drowned
    sheep_to_shore = total_sheep - sheep_drowned

    # L2
    multiplier_cows_drowned = 2 # Twice as many cows drowned as did sheep
    cows_drowned = multiplier_cows_drowned * sheep_drowned

    # L3
    total_cows = 10 # 10 cows
    cows_to_shore = total_cows - cows_drowned

    # L4
    total_dogs = 14 # 14 dogs
    total_to_shore = sheep_to_shore + cows_to_shore + total_dogs

    # FA
    answer = total_to_shore
    return answer