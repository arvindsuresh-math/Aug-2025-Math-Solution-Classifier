from fractions import Fraction

def solve():
    """Index: 7095.
    Returns: the total number of oysters and crabs counted in two days.
    """
    # L1
    oysters_day1 = 50 # 50 oysters on the rocks
    crabs_day1 = 72 # 72 crabs by the beach
    animals_day1 = oysters_day1 + crabs_day1

    # L2
    oysters_fraction_day2 = Fraction(1, 2) # only half the number of Oysters
    oysters_day2 = oysters_fraction_day2 * oysters_day1

    # L3
    crabs_fraction_day2 = Fraction(2, 3) # only 2/3 the number of crabs
    crabs_day2 = crabs_fraction_day2 * crabs_day1

    # L4
    animals_day2 = crabs_day2 + oysters_day2

    # L5
    total_animals = animals_day2 + animals_day1

    # FA
    answer = total_animals
    return answer