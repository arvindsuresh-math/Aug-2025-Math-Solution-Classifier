def solve():
    """Index: 6775.
    Returns: the total number of people coming to Iris' birthday party.
    """
    # L1
    num_son_per_unit = 1 # a son
    num_daughter_per_unit = 1 # a daughter
    num_aunt_uncle_per_unit = 1 # 1 aunt/uncle
    people_per_family_unit = num_son_per_unit + num_daughter_per_unit + num_aunt_uncle_per_unit

    # L2
    num_uncles = 3 # 3 uncles
    num_aunts = 4 # 4 aunts
    total_aunts_uncles = num_uncles + num_aunts

    # L3
    people_from_family_units = total_aunts_uncles * people_per_family_unit

    # L4
    num_mother = 1 # her mother
    num_brother = 1 # her brother
    total_people = people_from_family_units + num_mother + num_brother

    # FA
    answer = total_people
    return answer