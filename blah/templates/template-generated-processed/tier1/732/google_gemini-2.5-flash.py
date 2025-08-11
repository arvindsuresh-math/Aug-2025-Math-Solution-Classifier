def solve():
    """Index: 732.
    Returns: the total number of baby tarantula legs.
    """
    # L1
    num_sacs_total = 5 # 5 egg sacs
    num_sacs_less_one = 1 # one less than 5 egg sacs
    effective_egg_sacs = num_sacs_total - num_sacs_less_one

    # L2
    tarantulas_per_sac = 1000 # 1000 tarantulas
    total_tarantulas = effective_egg_sacs * tarantulas_per_sac

    # L3
    legs_per_tarantula = 8 # eight legs
    total_legs = total_tarantulas * legs_per_tarantula

    # FA
    answer = total_legs
    return answer