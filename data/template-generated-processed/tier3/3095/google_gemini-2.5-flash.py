from fractions import Fraction

def solve():
    """Index: 3095.
    Returns: the number of elephants in the Zoo.
    """
    # L1
    giraffes = 5 # 5 giraffes
    penguin_multiplier = 2 # twice as many penguins
    penguins = giraffes * penguin_multiplier

    # L2
    penguin_percentage_value = 20 # Penguins make up 20% of all the animals
    total_percentage_base = 100 # WK
    total_animals = total_percentage_base / penguin_percentage_value * penguins

    # L3
    elephant_percentage = Fraction(4, 100) # they make up 4% of all the animals
    elephants = elephant_percentage * total_animals

    # FA
    answer = elephants
    return answer