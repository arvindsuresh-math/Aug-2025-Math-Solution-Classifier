from fractions import Fraction

def solve():
    """Index: 2422.
    Returns: the total number of fish Hershel has remaining.
    """
    # L1
    initial_betta = 10 # 10 betta fish
    new_betta_fraction = Fraction(2, 5) # 2/5 times as many betta fish
    new_betta_fish = new_betta_fraction * initial_betta

    # L2
    total_betta_fish = new_betta_fish + initial_betta

    # L3
    initial_goldfish = 15 # 15 goldfish
    new_goldfish_fraction = Fraction(1, 3) # 1/3 times as many goldfish
    new_goldfish = new_goldfish_fraction * initial_goldfish

    # L4
    total_goldfish = initial_goldfish + new_goldfish

    # L5
    total_fish = total_betta_fish + total_goldfish

    # L6
    gift_divisor = 2 # gifts his sister 1/2 of the fish
    remaining_fish = total_fish / gift_divisor

    # FA
    answer = remaining_fish
    return answer