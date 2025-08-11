def solve():
    """Index: 101.
    Returns: the number of people Marcy is painting with makeup.
    """
    # L1
    num_tubs = 6 # Marcy decides to bring 6 tubs of lip gloss
    tubes_per_tub = 2 # each of which holds 2 tubes of lip gloss
    total_tubes = num_tubs * tubes_per_tub

    # L2
    people_per_tube = 3 # Each tube of lip gloss will hold enough lip gloss for 3 people's makeup
    total_people = total_tubes * people_per_tube

    # FA
    answer = total_people
    return answer