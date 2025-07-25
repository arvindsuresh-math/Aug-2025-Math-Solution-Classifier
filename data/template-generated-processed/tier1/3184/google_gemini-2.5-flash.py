def solve():
    """Index: 3184.
    Returns: the total number of animals bought on vacation.
    """
    # L1
    rick_guppies = 30 # Rick bought 30 guppies
    clowns_per_guppy_ratio = 2 # twice as many clowns as Rick bought guppies
    tim_clowns = clowns_per_guppy_ratio * rick_guppies

    # L2
    tetras_per_clown_ratio = 4 # 4 times as many tetras as Tim bought clowns
    my_tetras = tetras_per_clown_ratio * tim_clowns

    # L3
    total_animals = my_tetras + tim_clowns + rick_guppies

    # FA
    answer = total_animals
    return answer