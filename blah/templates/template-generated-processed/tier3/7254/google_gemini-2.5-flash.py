def solve():
    """Index: 7254.
    Returns: the number of classical CDs in Henry's collection.
    """
    # L1
    country_cds = 23 # 23 country CDs
    country_rock_difference = 3 # 3 more country CDs than rock CDs
    rock_cds = country_cds - country_rock_difference

    # L2
    rock_classical_multiplier = 2 # twice as many rock CDs as classical CDs
    classical_cds = rock_cds / rock_classical_multiplier

    # FA
    answer = classical_cds
    return answer