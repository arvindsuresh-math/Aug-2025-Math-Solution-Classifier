from fractions import Fraction

def solve():
    """Index: 2970.
    Returns: the total number of bunnies Marlon has now.
    """
    # L1
    initial_bunnies = 30 # 30 female baby bunnies
    fraction_given_away = Fraction(2, 5) # 2/5 of them to his friend Rodney
    bunnies_given_away = fraction_given_away * initial_bunnies

    # L2
    remaining_bunnies = initial_bunnies - bunnies_given_away

    # L3
    kittens_per_bunny = 2 # gave birth to 2 kittens each
    total_kittens_born = remaining_bunnies * kittens_per_bunny

    # L4
    total_bunnies = total_kittens_born + remaining_bunnies

    # FA
    answer = total_bunnies
    return answer