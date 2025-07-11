def solve():
    """Index: 1902.
    Returns: the total number of animals Josie counted.
    """
    # L1
    antelopes = 80 # 80 antelopes
    rabbits_more_than_antelopes = 34 # 34 more rabbits than antelopes
    rabbits = antelopes + rabbits_more_than_antelopes

    # L2
    total_rabbits_antelopes = rabbits + antelopes

    # L3
    hyenas_fewer_than_combined = 42 # 42 fewer hyenas
    hyenas = total_rabbits_antelopes - hyenas_fewer_than_combined

    # L4
    wild_dogs_more_than_hyenas = 50 # 50 more wild dogs than hyenas
    wild_dogs = hyenas + wild_dogs_more_than_hyenas

    # L5
    leopard_fraction_numerator = 1 # half the number of rabbits
    leopard_fraction_denominator = 2 # half the number of rabbits
    leopards = leopard_fraction_numerator / leopard_fraction_denominator * rabbits

    # L6
    total_animals = leopards + wild_dogs + hyenas + rabbits + antelopes

    # FA
    answer = total_animals
    return answer