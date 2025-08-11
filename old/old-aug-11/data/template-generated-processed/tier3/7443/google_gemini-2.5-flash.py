from fractions import Fraction

def solve():
    """Index: 7443.
    Returns: the age of Harry's mother when she gave birth to him.
    """
    # L1
    harry_age = 50 # Harry is 50 years old
    father_age_difference = 24 # His father is currently 24 years older than he is
    father_current_age = harry_age + father_age_difference

    # L2
    mother_age_fraction = Fraction(1, 25) # younger than his father by 1/25 of Harry's current age
    mother_age_difference_from_father = mother_age_fraction * harry_age

    # L3
    mother_current_age = father_current_age - mother_age_difference_from_father

    # L4
    mother_age_at_birth = mother_current_age - harry_age

    # FA
    answer = mother_age_at_birth
    return answer