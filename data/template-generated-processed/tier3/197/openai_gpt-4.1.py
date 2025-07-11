from fractions import Fraction

def solve():
    """Index: 197.
    Returns: the number of dinner rolls leftover after the party.
    """
    # L1
    total_people = 16 # There are 16 people at a dinner party
    half_divisor = 2 # Half the people
    half_people = total_people / half_divisor

    # L2
    rolls_per_person_group1 = Fraction(3, 2) # 1 1/2 rolls each
    rolls_eaten_group1 = half_people * rolls_per_person_group1

    # L3
    rolls_per_person_group2 = Fraction(1, 2) # 1/2 a roll each
    rolls_eaten_group2 = half_people * rolls_per_person_group2

    # L4
    total_rolls_eaten = rolls_eaten_group1 + rolls_eaten_group2

    # L5
    initial_rolls = 40 # There are 40 dinner rolls available
    rolls_leftover = initial_rolls - total_rolls_eaten

    # FA
    answer = rolls_leftover
    return answer