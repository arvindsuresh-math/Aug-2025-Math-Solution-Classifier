def solve():
    """Index: 732.
    Returns: the number of baby tarantula legs in one less than 5 egg sacs.
    """
    # L1
    egg_sacs_given = 5 # 5 egg sacs
    one_less = 1 # one less than 5
    num_egg_sacs = egg_sacs_given - one_less

    # L2
    tarantulas_per_sac = 1000 # one tarantula egg sac can contain 1000 tarantulas
    total_babies = num_egg_sacs * tarantulas_per_sac

    # L3
    legs_per_tarantula = 8 # tarantula has eight legs
    total_legs = total_babies * legs_per_tarantula

    # FA
    answer = total_legs
    return answer