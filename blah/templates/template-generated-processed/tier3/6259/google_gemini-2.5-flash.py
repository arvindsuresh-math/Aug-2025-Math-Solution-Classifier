from fractions import Fraction

def solve():
    """Index: 6259.
    Returns: the age difference between John and his mother.
    """
    # L1
    john_age_fraction = Fraction(1, 2) # half times younger
    father_age = 40 # John's father is 40 years old
    john_age = john_age_fraction * father_age

    # L2
    age_difference_father_mother = 4 # 4 years older than John's mother
    mother_age = father_age - age_difference_father_mother

    # L3
    age_difference_john_mother = mother_age - john_age

    # FA
    answer = age_difference_john_mother
    return answer