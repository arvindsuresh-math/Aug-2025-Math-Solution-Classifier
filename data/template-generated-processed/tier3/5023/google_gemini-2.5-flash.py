def solve():
    """Index: 5023.
    Returns: the amount of swords each orc has to carry.
    """
    # L1
    orcs_per_squad = 8 # 8 orcs each
    num_squads = 10 # 10 squads
    total_orcs = orcs_per_squad * num_squads

    # L2
    total_swords_pounds = 1200 # 1200 pounds of swords
    pounds_per_orc = total_swords_pounds / total_orcs

    # FA
    answer = pounds_per_orc
    return answer