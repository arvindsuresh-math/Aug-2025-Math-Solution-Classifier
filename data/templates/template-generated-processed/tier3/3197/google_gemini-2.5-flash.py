from fractions import Fraction

def solve():
    """Index: 3197.
    Returns: the number of pets Anthony has left.
    """
    # L1
    initial_pets = 16 # Anthony has 16 pets
    lost_pets = 6 # he lost 6 pets
    pets_after_loss = initial_pets - lost_pets

    # L2
    fraction_died = Fraction(1, 5) # 1/5 of his pets died
    pets_died_from_age = fraction_died * pets_after_loss

    # L3
    remaining_pets = pets_after_loss - pets_died_from_age

    # FA
    answer = remaining_pets
    return answer