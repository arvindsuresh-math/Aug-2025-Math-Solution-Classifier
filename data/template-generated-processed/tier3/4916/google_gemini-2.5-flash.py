from fractions import Fraction

def solve():
    """Index: 4916.
    Returns: the remaining number of fruits in the bag.
    """
    # L1
    initial_apples = 7 # seven apples
    apples_taken = 2 # two apples
    remaining_apples = initial_apples - apples_taken

    # L2
    oranges_multiplier = 2 # twice as many oranges as apples
    oranges_taken = apples_taken * oranges_multiplier

    # L3
    initial_oranges = 8 # eight oranges
    remaining_oranges = initial_oranges - oranges_taken

    # L4
    mangoes_fraction = Fraction(2, 3) # 2/3 the number of mangoes
    initial_mangoes = 15 # 15 mangoes
    mangoes_taken = mangoes_fraction * initial_mangoes

    # L5
    remaining_mangoes = initial_mangoes - mangoes_taken

    # L6
    total_remaining_fruits = remaining_apples + remaining_oranges + remaining_mangoes

    # FA
    answer = total_remaining_fruits
    return answer