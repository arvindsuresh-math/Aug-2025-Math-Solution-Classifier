def solve():
    """Index: 4591.
    Returns: the number of sodas left over when the party is over.
    """
    # L1
    num_packs = 3 # 3 12-packs of soda
    sodas_in_a_pack = 12 # 12-packs of soda
    initial_sodas = num_packs * sodas_in_a_pack

    # L2
    total_people = 6 # 6 people are at the party
    half_divisor = 2 # Half of the people
    people_in_half_group = total_people / half_divisor

    # L3
    sodas_per_person_half_group = 3 # 3 sodas each
    sodas_drank_by_half_group = people_in_half_group * sodas_per_person_half_group

    # L4
    num_people_group2 = 2 # 2 of the people
    sodas_per_person_group2 = 4 # 4
    sodas_drank_by_group2 = num_people_group2 * sodas_per_person_group2

    # L5
    sodas_drank_by_group3 = 5 # 1 person has 5
    total_sodas_drank = sodas_drank_by_group3 + sodas_drank_by_half_group + sodas_drank_by_group2

    # L6
    sodas_left = initial_sodas - total_sodas_drank

    # FA
    answer = sodas_left
    return answer