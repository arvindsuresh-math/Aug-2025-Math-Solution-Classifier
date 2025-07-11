def solve():
    """Index: 1449.
    Returns: the total number of animals Erica saw.
    """
    # L1
    lions_saturday = 3 # 3 lions
    elephants_saturday = 2 # 2 elephants
    animals_saturday = lions_saturday + elephants_saturday

    # L2
    buffaloes_sunday = 2 # 2 buffaloes
    leopards_sunday = 5 # 5 leopards
    animals_sunday = buffaloes_sunday + leopards_sunday

    # L3
    rhinos_monday = 5 # 5 rhinos
    warthogs_monday = 3 # 3 warthogs
    animals_monday = rhinos_monday + warthogs_monday

    # L4
    total_animals = animals_saturday + animals_sunday + animals_monday

    # FA
    answer = total_animals
    return answer