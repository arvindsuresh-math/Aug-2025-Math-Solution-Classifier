from fractions import Fraction

def solve():
    """Index: 5688.
    Returns: the number of girls in the class who have no pet.
    """
    # L1
    total_fraction = 1 # WK
    boys_fraction = Fraction(1, 3) # 1/3 of them are boys
    girls_fraction = total_fraction - boys_fraction

    # L2
    total_students = 30 # 30 students
    num_girls = total_students * girls_fraction

    # L3
    total_percent = 100 # WK
    percent_own_dogs = 40 # 40% own dogs
    percent_own_cat = 20 # 20% own a cat
    percent_no_pets = total_percent - percent_own_dogs - percent_own_cat

    # L4
    percent_no_pets_decimal = percent_no_pets / 100
    girls_no_pets = num_girls * percent_no_pets_decimal

    # FA
    answer = girls_no_pets
    return answer