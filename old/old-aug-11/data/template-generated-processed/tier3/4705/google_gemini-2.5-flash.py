from fractions import Fraction

def solve():
    """Index: 4705.
    Returns: the remaining kilograms of meat.
    """
    # L1
    initial_meat_kg = 20 # Jackson had 20 kilograms of meat
    meatball_fraction = Fraction(1, 4) # 1/4 of the meat
    meat_for_meatballs = initial_meat_kg * meatball_fraction

    # L2
    meat_after_meatballs = initial_meat_kg - meat_for_meatballs

    # L3
    meat_for_spring_rolls = 3 # used 3 kilograms of meat to make spring rolls
    remaining_meat = meat_after_meatballs - meat_for_spring_rolls

    # FA
    answer = remaining_meat
    return answer