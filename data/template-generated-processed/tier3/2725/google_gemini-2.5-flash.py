from fractions import Fraction

def solve():
    """Index: 2725.
    Returns: the total number of puppies Tenisha remains with.
    """
    # L1
    total_dogs = 40 # 40 dogs
    female_percentage = Fraction(60, 100) # 60% of them are female
    female_dogs = female_percentage * total_dogs

    # L2
    birth_fraction = Fraction(3, 4) # 3/4 of the female gives birth
    female_dogs_giving_birth = birth_fraction * female_dogs

    # L3
    puppies_per_dog = 10 # 10 puppies each
    total_puppies_born = female_dogs_giving_birth * puppies_per_dog

    # L4
    donated_puppies = 130 # donating 130 puppies to the church
    remaining_puppies = total_puppies_born - donated_puppies

    # FA
    answer = remaining_puppies
    return answer