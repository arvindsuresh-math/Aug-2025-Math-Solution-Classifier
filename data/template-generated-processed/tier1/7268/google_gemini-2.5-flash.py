def solve():
    """Index: 7268.
    Returns: the number of sheep Mr. Bodhi added to the yacht.
    """
    # L1
    num_cows = 20 # 20 cows
    num_foxes = 15 # 15 foxes
    cows_and_foxes = num_cows + num_foxes

    # L2
    zebra_multiplier = 3 # three times as many zebras as foxes
    num_zebras = zebra_multiplier * num_foxes

    # L3
    total_animals_so_far = cows_and_foxes + num_zebras

    # L4
    required_total_animals = 100 # total number of animals in the yacht needs to be 100
    sheep_to_add = required_total_animals - total_animals_so_far

    # FA
    answer = sheep_to_add
    return answer