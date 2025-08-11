def solve():
    """Index: 1148.
    Returns: the number of grains of rice in a teaspoon.
    """
    # L1
    tablespoons_per_half_cup = 8 # half a cup is 8 tablespoons
    half_cups_per_cup = 2 # WK
    tablespoons_per_cup = tablespoons_per_half_cup * half_cups_per_cup

    # L2
    teaspoons_per_tablespoon = 3 # one tablespoon is 3 teaspoons
    teaspoons_per_cup = tablespoons_per_cup * teaspoons_per_tablespoon

    # L3
    grains_per_cup = 480 # 480 grains of rice in one cup
    grains_per_teaspoon = grains_per_cup / teaspoons_per_cup

    # FA
    answer = grains_per_teaspoon
    return answer