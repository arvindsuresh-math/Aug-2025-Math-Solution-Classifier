def solve():
    """Index: 101.
    Returns: the total number of people Marcy is painting with makeup.
    """
    # L1
    num_tubs_brought = 6 # 6 tubs of lip gloss
    tubes_per_tub = 2 # 2 tubes of lip gloss
    total_tubes = num_tubs_brought * tubes_per_tub

    # L2
    people_per_tube = 3 # 3 people's makeup
    total_people = total_tubes * people_per_tube

    # FA
    answer = total_people
    return answer