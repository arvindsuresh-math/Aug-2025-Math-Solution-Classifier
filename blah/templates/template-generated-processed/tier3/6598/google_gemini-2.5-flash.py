from fractions import Fraction

def solve():
    """Index: 6598.
    Returns: the number of female fish Ariel has.
    """
    # L1
    total_fraction = 1 # WK
    male_fraction = Fraction(2, 3) # 2/3 are male
    female_fraction = total_fraction - male_fraction

    # L2
    total_fish = 45 # She has 45 fish
    female_fish = total_fish * female_fraction

    # FA
    answer = female_fish
    return answer