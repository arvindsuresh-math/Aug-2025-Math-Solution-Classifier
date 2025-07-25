from fractions import Fraction

def solve():
    """Index: 3654.
    Returns: the total number of animals Philip has on his farm.
    """
    # L1
    duck_percentage_increase = Fraction(50, 100) # 50% more ducks
    cows = 20 # 20 cows
    additional_ducks = duck_percentage_increase * cows

    # L2
    total_ducks = cows + additional_ducks

    # L3
    total_cows_and_ducks = cows + total_ducks

    # L4
    pig_fraction = Fraction(1, 5) # one-fifth of ducks and cows in total
    total_pigs = pig_fraction * total_cows_and_ducks

    # L5
    total_animals = total_cows_and_ducks + total_pigs

    # FA
    answer = total_animals
    return answer